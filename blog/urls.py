from blog.views import *
from user_auth.views import *
from django.urls import path


urlpatterns = [
    path('articles', ArticlesListView.as_view(), name='articles'),
    path('article/<int:id>', ArticleDetailView.as_view(), name='art_detail'),
    path('users', UserListView.as_view(), name='users'),
    path('user_detailed/<int:id>', UserDetailView.as_view(), name='user_det'),
]