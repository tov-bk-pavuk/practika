from user_auth.views import *
from django.urls import include, path

urlpatterns = [
    path('create', CreateProfile.as_view(), name='crt_profile'),
    path('update', UpdateProfile.as_view(), name='upd_profile'),
    path('profile', UserProfile.as_view(), name='profile'),
    path('logout', UserLogout.as_view(), name='logout'),
    path('thanks', thanks, name='thanks'),
]