from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager
from django.shortcuts import reverse


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('Username'), max_length=50, unique=True, blank=False)
    fullname = models.CharField(_('Full name'), max_length=200, unique=True, blank=False)
    email = models.EmailField(_('email address'), unique=True, blank=False)
    gender = models.CharField(_('Gender'), max_length=10, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')])
    dob = models.DateField(_('Date of Birth'))
    bio = models.TextField(_('Tell about yourself'))
    profile_pic = models.ImageField(upload_to='users/profile_pics', default='users/profile_pics/default.jpg')
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'fullname', 'dob', 'gender', 'bio', 'profile_pic']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("users:my_profile")