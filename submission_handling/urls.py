
from django.urls import path
from .views import submit_code, view_submissions

urlpatterns = [
    path('submit/', submit_code, name='submit_code'),
    path('view/<int:submission_id>/', view_submissions, name='view_submission'),
]
