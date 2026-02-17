from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/', views.category, name='category'),
    path('single/', views.single, name='single'),
    path('contact/', views.contact, name='contact'),
]


