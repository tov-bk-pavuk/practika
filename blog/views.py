from blog.models import *
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from user_auth.forms import User


class ArticlesListView(ListView):
    model = Article
    template_name = 'blog/articles.html'
    queryset = Article.objects.all()
    paginate_by = 10


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
