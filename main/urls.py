from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('faq', views.faq, name='faq'),
    path('<str:pk>/', views.WritersDetailView.as_view(), name='writer') 
] 

 