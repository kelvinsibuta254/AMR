from django.db import models
from BlogApplication import settings
from django.contrib.auth.models import User


# Create your models here.
#User = settings.AUTH_USER_MODEL
class Gene(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)