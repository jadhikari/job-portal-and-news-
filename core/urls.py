from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('news/', views.news_home, name='news'),
    path('news/<str:unique_id>/', views.news_detail, name='news_detail'),
    path('contact/', views.contact, name='contact'),
    
]
