from django.db import models
from django.contrib.auth.models import User

class Smoothie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.title
