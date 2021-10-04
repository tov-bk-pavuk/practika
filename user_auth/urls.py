from user_auth.views import CreateProfile, UserProfile, UpdateProfile, thanks
from django.urls import include, path

urlpatterns = [
    path('create', CreateProfile.as_view(), name='crt_profile'),
    path('update', UpdateProfile.as_view(), name='upd_profile'),
    path('delete', UserProfile.as_view(), name='profile'),
    path('thanks', thanks, name='thanks'),
]