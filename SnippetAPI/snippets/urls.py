from django.urls import path
from snippets import views
from .views import *

urlpatterns = [

    # SNIPPET
    path('get_snippets/',GetSnippetListView.as_view()),
    path('post_snippets/',PostSnippetListView.as_view()),
    path('get_snippets_by_pk/<int:pk>/',GetSnippetDetailView.as_view()),
    path('put_snipptes_by_pk/<int:pk>/',PutSnippetDetailView.as_view()),
    path('delete_snippets_by_pk/<int:pk>/',DeleteSnippetView.as_view()),

    # STUDENT
    path('get_student/',GetStudentListView.as_view()),
    path('post_student/',PostStudentListView.as_view()),
    path('get_student_by_pk/<int:pk>/',GetStudentDetailView.as_view()),
    path('put_student_by_pk/<int:pk>/',PutStudentlistView.as_view()),
    path('delete_student_by_pk/<int:pk>/',DeleteStudentListView.as_view()),

    # EMPLOYEE
    path('get_employee/',GetEmployeeListView.as_view()),
    path('post_student/',PostEmployeeListView.as_view()),
    path('get_employee_by_pk/<int:pk>/',RetrieveEmployeeListView.as_view()),
    path('put_employee_by_pk/<int:pk>/',PutEmployeeListView.as_view()),
    path('delete_student_by_pk/<int:pk>/',DeleteEmployeeListView.as_view()),

]
