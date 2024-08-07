from django.urls import path
from main import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('faq', views.FAQView.as_view(), name='faq'),
    path('<str:pk>/', views.WritersDetailView.as_view(), name='writer') 
] 
