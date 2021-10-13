from blog.models import *
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from user_auth.forms import *


class ArticlesListView(ListView):
    model = Article
    template_name = 'blog/articles.html'
    queryset = Article.objects.filter(published=True)
    paginate_by = 10


def create_article(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = NewArticle(request.POST)
            if form.is_valid():
                title = form.cleaned_data['text']
                short_description = form.cleaned_data['short_description']
                text = form.cleaned_data['text']
                published = form.cleaned_data['published']
                user = request.user
                Article.objects.create(title=title, short_description=short_description,
                                       text=text, author=user, published=published)
                return HttpResponseRedirect('../../accounts/profile')
        else:
            form = NewArticle()
        return render(request, 'blog/article_create.html', {'form': form})
    return HttpResponseRedirect('../../accounts/login')


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    pk_url_kwarg = 'id'
    template_name = 'blog/article_update.html'
    form_class = NewArticle
    success_url = '../../accounts/profile'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detailed.html'
    pk_url_kwarg = 'id'


class UserListView(ListView):
    model = User
    template_name = 'blog/users.html'
    queryset = User.objects.exclude(is_staff=True).all()
    paginate_by = 10


class UserDetailView(DetailView):
    model = User
    template_name = 'blog/user_detailed.html'
    pk_url_kwarg = 'id'


class CommentListView(ListView):
    model = Comment
    template_name = 'blog/comments.html'
    queryset = Comment.objects.filter(is_published=True).all()
    paginate_by = 20


def comment_create(request, id):
    if request.method == 'POST':
        form = NewComment(request.POST)
        article = Article.objects.get(pk=id)
        username = request.user
        if form.is_valid():
            text = form.cleaned_data['text']
            article = Article.objects.get(pk=id)
            if request.user.is_authenticated:
                Comment.objects.create(article=article, username=username, text=text)
            else:
                Comment.objects.create(article=article, text=text)
            return HttpResponseRedirect('../../article/' + str(id))  # /thanks/
    else:
        form = NewComment()
        article = Article.objects.get(pk=id)
    return render(request, 'blog/comment_create.html', {'form': form, 'article': article})
