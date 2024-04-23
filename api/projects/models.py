# Create your models here.

from django.db import models

class Projects(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    companies = models.TextField()
    content = models.TextField()
    duration = models.TextField()
    imageUrl = models.TextField()

    def __str__(self):
        return self.name

