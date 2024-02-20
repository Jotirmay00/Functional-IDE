# code_execution/urls.py

from django.urls import path
from .views import evaluate_code

urlpatterns = [
    path('evaluate/', evaluate_code, name='evaluate_code'),
]
