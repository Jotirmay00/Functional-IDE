# submissions/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_code, name='submit_code'),
    path('view/', views.view_submissions, name='view_submissions'),
]
