from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
