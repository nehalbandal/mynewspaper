from django.shortcuts import redirect
from .models import NewsArticle
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
import newspaper
import validators
from django.contrib import messages

import joblib
import os
current_dir_path = os.path.join(os.path.dirname(__file__))
news_classifier = joblib.load(os.path.join(current_dir_path)+ "/ml_model/news_classifier.pkl")
fake_news_classifier = joblib.load(os.path.join(current_dir_path)+ "/ml_model/fake_news_classifier.pkl")

import nltk
nltk.download('punkt')

def get_news_articles(request):
    if request.method == 'POST':
        url = request.POST.get('news_url')
        if not validators.url(url):
            messages.error(request, 'Invalid URL.')
            print("Invalid URL")
            return redirect("news:news_list")
        site = newspaper.build(url, memoize_articles=False)
        site.article_urls()
        print("Total Articles: ", len(site.articles))
        n_articles = 10 if len(site.articles)>= 10 else len(site.articles)
        for index in range(n_articles):
            article = site.articles[index]
            article.download()
            article.parse()
            article.nlp()
            news_article = NewsArticle()
            news_article.website = url
            news_article.title = article.title
            news_article.summary = article.summary
            news_article.url = article.url
            news_article.image = article.top_image
            news_article.user = request.user
            news_article.category = news_classifier.predict([article.summary,])[0]
            news_article.is_real = fake_news_classifier.predict([article.summary,])[0]
            news_article.save()
            print("===== Article {} Saved ====", news_article.title)
    return redirect("news:news_list")


class NewsList(LoginRequiredMixin, ListView):
    paginate_by = 10
    model = NewsArticle
    template_name = 'news/news_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        queryset = queryset.order_by('-fetched_date')
        if self.kwargs.get('news_cat'):
            queryset = queryset.filter(category=self.kwargs['news_cat'])
            print(self.kwargs['news_cat'], queryset.count())
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['news_category'] = list(NewsArticle.objects.all().values('category').distinct())
        return context