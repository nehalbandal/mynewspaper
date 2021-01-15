from django.urls import path
from .views import get_news_articles, NewsList

app_name = 'news'

urlpatterns = [
  path('', NewsList.as_view(), name="news_list"),
  path('<str:news_cat>', NewsList.as_view(), name="news_list"),
  path('get_news_articles/', get_news_articles, name="get_news_articles"),
]