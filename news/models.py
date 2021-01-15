from django.db import models
from django.conf import settings
from django.utils import timezone


class NewsArticle(models.Model):
    website = models.URLField()
    title = models.CharField(max_length=500, blank=True)
    image = models.URLField(null=True, blank=True)
    summary = models.TextField()
    url = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='news_articles', on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='Unknown')
    fetched_date = models.DateTimeField(default=timezone.now)
    is_real = models.CharField(max_length=255, default='REAL')
    
    def __str__(self):
        return self.title
