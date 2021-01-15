from django.contrib import admin
from .models import NewsArticle


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_real', 'user']
    list_filter = ['category', 'is_real', 'user']


admin.site.register(NewsArticle, NewsAdmin)