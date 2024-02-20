# submission_handling/serializers.py

from rest_framework import serializers
from .models import Submission

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'code', 'test_cases', 'verdict', 'timestamp']
