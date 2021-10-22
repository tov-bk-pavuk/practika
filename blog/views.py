from blog.tasks import *
from blog.urls import *

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    DetailView,
    ListView,
    UpdateView,
)
from user_auth.forms import *


def contact_form(request):
    data = dict()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            notify_contact.apply_async(kwargs={
                'name': name,
                'email': email,
                'text': text
            })
            data['form_is_valid'] = True
            data['html_form'] = render_to_string('blog/contact_form_success.html')
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string('blog/contact_form.html', context, request)
    # render_to_string это функция, которая рендерит 'request', при помощи Шаблона, передавая туда 'context'
    return JsonResponse(data)


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
                title = form.cleaned_data['title']
                short_description = form.cleaned_data['short_description']
                text = form.cleaned_data['text']
                published = form.cleaned_data['published']
                user = request.user
                a = Article.objects.create(title=title, short_description=short_description,
                                       text=text, author=user, published=published)
                url = f'http://127.0.0.1:8000' + reverse_lazy('art_detail', args=[a.pk])
                notify.apply_async(kwargs={'mas': f'Новая статья: от {user.username}'
                                                  f' {title}, ссылка {url}'})
                return HttpResponseRedirect(reverse('profile'))
        else:
            form = NewArticle()
        return render(request, 'blog/article_create.html', {'form': form})
    return HttpResponseRedirect(reverse('login'))


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    pk_url_kwarg = 'id'
    template_name = 'blog/article_update.html'
    form_class = NewArticle
    success_url = reverse_lazy('profile')


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
            if request.user.is_authenticated:
                email = request.user.email
                url = 'http://127.0.0.1:8000' + reverse_lazy('art_detail', args=[id])
                if email != '':
                    notify_user.apply_async(kwargs={
                        'mas': f'Новый комментарий к статье {article.title}: {text}, {url}',
                        'email': f'{email}'
                    })
                Comment.objects.create(article=article, username=username, text=text)
            else:
                Comment.objects.create(article=article, text=text)
            return HttpResponseRedirect(reverse_lazy('art_detail', args=[id]))
    else:
        form = NewComment()
        article = Article.objects.get(pk=id)
    return render(request, 'blog/comment_create.html', {'form': form, 'article': article})
