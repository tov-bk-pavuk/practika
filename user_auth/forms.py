from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from blog.models import Article


User = get_user_model()


class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class NewArticle(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'