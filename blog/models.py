from django.db import models
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=250)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text
