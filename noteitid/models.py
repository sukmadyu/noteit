from django.db import models
from django.utils import timezone

# Create your models here.
class Comments(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=12)
    message=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
