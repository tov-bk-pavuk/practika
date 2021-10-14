from django.contrib import admin

from .models import Article, Comment


class BookInline(admin.TabularInline):
    model = Article
    extra = 1


@admin.action(description='Mark selected as published')
def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Mark selected as UNpublished')
def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_published=False)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'short_description', 'text', 'author']
    search_fields = ['title']
    actions = [make_published, make_unpublished]
    list_display = ('title', 'short_description', 'author')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['username', 'article', 'text', 'is_published']
    search_fields = ['username']
    actions = [make_published, make_unpublished]
    list_display = ('username', 'article', 'text', 'is_published')


