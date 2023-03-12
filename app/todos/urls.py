from django.conf.urls import include
from django.urls import path
from .views import ListTodo, DetailTodo

urlpatterns = [
    path('', ListTodo.as_view()),
    path('/<int:pk>/', DetailTodo.as_view()),
    path('/show/<int:pk>/', DetailTodo.as_view()),
]
