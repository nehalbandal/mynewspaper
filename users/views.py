from django.views.generic import TemplateView, CreateView, UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin


class Registration(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/registration.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Registration'
        return context

class UpdateUserProfile(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/update_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'My Profile'
        return context


class UserProfile(LoginRequiredMixin, TemplateView):
    template_name = 'users/my_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['websites_scrapped'] = list(self.request.user.news_articles.all().values('website').distinct())
        context['title'] = 'User Profile'
        return context