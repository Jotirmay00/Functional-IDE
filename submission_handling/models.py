from django.db import models
from django.contrib.auth.models import User

class Submission(models.Model):
    code = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.user.username} at {self.timestamp}"
