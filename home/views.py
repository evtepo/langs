from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponse, Http404

from .models import *

from random import choice


def index(request):  #  Главная страница
    cats = Category.objects.all()
    posts = Languages.objects.all()
    context = {
        'cat_selected': 0,
        'cats': cats,
        'posts': posts,
    }

    return render(request, "home/index.html", context=context)


def signin(request):  #  Вход
    return render(request, 'home/signin.html')


def show_category(request, cat_slug):  #  Показывает категории
    cats = Category.objects.all()
    posts = Languages.objects.filter(category__slug=cat_slug)

    context = {
        'cats': cats,
        'posts': posts,
        'cat_selected': cat_slug
    }

    if len(posts) == 0:
        raise Http404()

    return render(request, 'home/index.html', context=context)


def show_post(request, post_slug):  #  Показывает отдельный пост
    post = get_object_or_404(Languages, slug=post_slug)

    context = {
        'post': post,
        'cat_selected': post.category,
    }

    return render(request, 'home/post.html', context=context)


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