# Generated by Django 3.1.3 on 2021-01-14 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField()),
                ('title', models.CharField(blank=True, max_length=500)),
                ('image', models.URLField(blank=True, null=True)),
                ('summary', models.TextField()),
                ('url', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]