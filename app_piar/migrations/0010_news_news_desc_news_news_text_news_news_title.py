# Generated by Django 4.2.7 on 2023-12-14 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_piar', '0009_remove_news_news_desc_remove_news_news_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_desc',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='news_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='news_title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]