# Generated by Django 3.1.3 on 2021-01-15 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_newsarticle_is_true'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsarticle',
            name='is_true',
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='is_real',
            field=models.CharField(default='Real', max_length=255),
        ),
    ]
