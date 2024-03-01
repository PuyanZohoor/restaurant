from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index_page, name = 'index'),
    path('about', views.about_page, name = 'about'),
    path('book', views.book_page, name = 'book'),
    path('menu', views.menu_page, name = 'menu'),
]