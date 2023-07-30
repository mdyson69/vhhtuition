from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_assessments, name='assessments'),
    path('<int:assessment_id>/', views.assessment_questions,
         name='assessment_questions'),
    path('assessment_management/', views.assessment_management,
         name='assessment_management'),
    path('question_management/<int:assessment_id>', views.question_management,
         name='question_management'),
    path('edit_assessment/<int:assessment_id>/',
         views.edit_assessment, name='edit_assessment'),
    path('edit_question/<int:question_id>/',
         views.edit_question, name='edit_question'),
    path('add_question/', views.add_question, name='add_question'),
    path('delete_question/<int:question_id>/',
         views.delete_question, name='delete_question'),
    path('add_assessment/', views.add_assessment, name='add_assessment'),
    path('delete_assessment/<int:assessment_id>/',
         views.delete_assessment, name='delete_assessment'),
]
