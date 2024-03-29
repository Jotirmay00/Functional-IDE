# submissions/models.py
from django.db import models

class Submission(models.Model):
    code = models.TextField() 
    timestamp = models.DateTimeField(auto_now_add=True)
    verdict = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Submission at {self.timestamp}"
