from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_courses, name='display_courses'),
    path('<int:course_id>/', views.view_course,
         name='view_course'),
    path('course_management/', views.course_management,
         name='course_management'),
    path('add_course/', views.add_course, name='add_course'),
    path('edit_course/<int:course_id>/',
         views.edit_course, name='edit_course'),
    path('delete_course/<int:course_id>/',
         views.delete_course, name='delete_course'),
]
