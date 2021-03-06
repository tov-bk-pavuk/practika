from blog.views import *
from user_auth.views import *
from django.urls import path


urlpatterns = [
    path('contact_form', contact_form, name='contact_form'),
    path('articles', ArticlesListView.as_view(), name='articles'),
    path('article/create', create_article, name='art_create'),
    path('article/<int:id>', ArticleDetailView.as_view(), name='art_detail'),
    path('article/update/<int:id>', ArticleUpdateView.as_view(), name='art_update'),
    path('comments', CommentListView.as_view(), name='comments'),
    path('comment/create/<int:id>', comment_create, name='comment_create'),
    path('users', UserListView.as_view(), name='users'),
    path('user_detailed/<int:id>', UserDetailView.as_view(), name='user_det'),
]