from django.contrib.auth.models import User
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers, serializers, viewsets

from blog.views import UserViewSet, GroupViewSet, ArticleViewSet, CommentViewSet

from user_auth.views import *


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('', home, name='home'),
    path('', include('blog.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('user_auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
