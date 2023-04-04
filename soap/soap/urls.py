from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from home import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LanguagesListView.as_view(), name='home'),
    path('signin/', views.LoginUser.as_view(), name='signin'),
    path('post/<slug:post_slug>/', views.PostView.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.CategoryLanguages.as_view(), name='category'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
    path('random/', views.random, name='random'),
    path('contacts/', views.contacts, name='contacts'),
    path('registration/', views.RegisterUsers.as_view(), name='registration'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = views.pageNotFound
