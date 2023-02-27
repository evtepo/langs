from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

from .forms import *
from .models import *
from .utils import *
from random import choice


#  Отображение всех постов из модели Languages
class LanguagesListView(DataMixin, ListView):
    model = Languages
    template_name = 'home/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_from_mixin = self.get_user_context(title='Langs')
        return dict(list(context.items()) + list(context_from_mixin.items()))

    def get_queryset(self):
        return Languages.objects.all().select_related('category')


#  Отображение постов по категориям 
class CategoryLanguages(DataMixin, ListView):
    model = Languages
    template_name = 'home/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        context_from_mixin = self.get_user_context(title='Категоря: ' + str(c.name))
        return dict(list(context.items()) + list(context_from_mixin.items()))
    
    def get_queryset(self):
        return Languages.objects.filter(category__slug=self.kwargs['cat_slug'], is_published=True).select_related('category')


# Отображение определенного поста
class PostView(DataMixin, DetailView):
    model = Languages
    template_name = 'home/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_from_mixin = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(context_from_mixin.items()))    


#  Профиль
def profile(request):
    return HttpResponse(f'Профиль')


#  Рандомный язык
def random(request):
    random_lang = choice(Languages.objects.all())
    cats = Category.objects.all()
    context = {
        'random_lang': random_lang,
        'cats': cats,
    }

    return render(request, 'home/random.html', context=context)


#  Контакты
def contacts(request):
    return HttpResponse(f'Contacts')


#  Регистрация
class RegisterUsers(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'home/registration.html'
    success_url = reverse_lazy('signin')

    def get_context_data(self, **kwargs):
        context = super().get_user_context(**kwargs)
        context_from_mixin = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(context_from_mixin.items()))
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    

# Вход
class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'home/signin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_from_mixin = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(context_from_mixin.items()))
    

#  Выход
def logout_user(request):
    logout(request)
    return redirect('signin')


#  Страница не найдена
def pageNotFound(request, exception):
    return HttpResponseNotFound(f'Страница не найдена')
