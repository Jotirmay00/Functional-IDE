
from rest_framework import serializers

class CodeEvaluationSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=None, allow_blank=False)
