from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from blog.models import *


User = get_user_model()


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           label='Ваше имя',
                           widget=forms.TextInput(attrs={
                               'placeholder': 'Имя',
                               'class': 'form-control'
                           }))
    email = forms.EmailField(label='Email',
                             widget=forms.TextInput(attrs={
                                 'placeholder': 'i.ivanov@gmail.com',
                                 'class': 'form-control'
                             }))
    text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'сообщение', 'class': 'form-control'}))


class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class NewArticle(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'short_description', 'text', 'published']  # 'author'


class NewComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
