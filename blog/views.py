from blog.models import *
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
    queryset = Article.objects.all()
    paginate_by = 10


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'blog/article_create.html'
    form_class = NewArticle
    success_url = '../articles'


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
    queryset = Comment.objects.all()
    paginate_by = 20


def comment_create(request, id):
    if request.method == 'POST':
        form = NewComment(request.POST)
        article = Article.objects.get(pk=id)
        username = request.user
        if form.is_valid():
            text = form.cleaned_data['text']
            article = Article.objects.get(pk=id)
            Comment.objects.create(article=article, username=username, text=text)
            return HttpResponseRedirect('../../article/' + str(id))  # /thanks/
    else:
        form = NewComment()
        article = Article.objects.get(pk=id)
    return render(request, 'blog/comment_create.html', {'form': form, 'article': article})
