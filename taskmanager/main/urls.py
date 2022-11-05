
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('catalog/', views.catalog, name='catalog'),
    path('news/', views.news, name='news'),
    path('news/news_1/', views.news_1, name='news_1'),
    path('about/', views.about, name='about'),
    path('obr_sv/', views.obr_sv, name='obr_sv'),
    path('gde_kupit/', views.gde_kupit, name='gde_kupit'),
]
