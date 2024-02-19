# submissions/models.py
from django.db import models

class Submission(models.Model):
    code = models.TextField()
    test_cases = models.TextField(default ="")  # Field to store test cases (assuming they are provided as JSON)
    verdict = models.CharField(max_length=50, blank=True)  # Field to store the verdict of code evaluation
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission at {self.timestamp}"
