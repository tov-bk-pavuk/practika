from django.db import models
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название статьи', unique=True)
    short_description = models.CharField(max_length=250, verbose_name='Краткое описание')
    text = models.TextField(verbose_name='Текст статьи')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        unique_together = ['title', 'short_description']

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=250, verbose_name='Текст комментария')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.text
