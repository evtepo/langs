from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponse, Http404
from django.views.generic import ListView, DetailView

from .models import *

from random import choice


class LanguagesListView(ListView):  #  Отображение всех постов из модели Languages
    model = Languages
    template_name = 'home/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Langs'
        context['cats'] = Category.objects.all()
        return context

    def get_queryset(self):
        return Languages.objects.all()


def signin(request):  #  Вход
    return render(request, 'home/signin.html')


class CategoryLanguages(ListView):  #  Отображение постов по категориям 
    model = Languages
    template_name = 'home/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория: ' + str(context['posts'][0].category)
        context['cats'] = Category.objects.all()
        return context

    def get_queryset(self):
        return Languages.objects.filter(category__slug=self.kwargs['cat_slug'], is_published=True)


class PostView(DetailView): # Отображение определенного поста
    model = Languages
    template_name = 'home/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['cats'] = Category.objects.all()      
        return context


def profile(request):  #  Профиль
    return HttpResponse(f'Профиль')


def random(request):  #  Рандомный язык
    random_lang = choice(Languages.objects.all())
    context = {
        'random_lang': random_lang
    }

    return render(request, 'home/random.html', context=context)


def contacts(request):  #  Контакты
    return HttpResponse(f'Contacts')


def pageNotFound(request, exception):  #  Страница не найдена
    return HttpResponseNotFound(f'Страница не найдена')