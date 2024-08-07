from django.urls import path
from . import views
from main.views import WritersDetailView

urlpatterns = [
    path('', views.bio_home, name='bio_home'),
    path('pushkin', views.bio_pushkin, name='bio_pushkin'),
    path('akhmatova', views.bio_akhmatova, name='bio_akhmatova'),
    path('dostoevsky', views.bio_dostoevsky, name='bio_dostoevsky'),
    path('esenin', views.bio_esenin, name='bio_esenin'),
    path('gorky', views.bio_gorky, name='bio_gorky'),
    path('lermontov', views.bio_lermontov, name='bio_lermontov'),
    path('mayakovsky', views.bio_mayakovsky, name='bio_mayakovsky'),
    path('tsvetaeva', views.bio_tsvetaeva, name='bio_tsvetaeva')
] 
