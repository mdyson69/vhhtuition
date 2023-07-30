from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('my_courses/<order_number>', views.my_courses,
         name='my_courses'),
]
