from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact_success/<contact_number>',
         views.contact_success,
         name='contact_success'),
    path('messages/', views.message_management, name='message_management'),
    path('delete_messages/<int:contact_id>/',
         views.delete_message, name='delete_message'),
]
