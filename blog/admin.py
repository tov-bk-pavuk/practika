from django.contrib import admin

from .models import Article, Comment


class BookInline(admin.TabularInline):
    model = Article
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'short_description', 'text', 'author']
    search_fields = ['title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['username', 'article', 'text']
    search_fields = ['username']
