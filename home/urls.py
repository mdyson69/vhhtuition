from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('cookie-policy/', views.cookie, name='cookie'),
]
