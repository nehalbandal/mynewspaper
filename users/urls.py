from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='users'

urlpatterns = [ path('registration/', views.Registration.as_view(), name='register'),
                path('myprofile/', views.UserProfile.as_view(), name='my_profile'),
                path('myprofile/<int:pk>/edit/', views.UpdateUserProfile.as_view(), name='profile_edit'),
                path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
                path('logout/', auth_views.LogoutView.as_view(), name='logout'),] \

