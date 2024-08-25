from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class CustomUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    createdAt = models.DateField(auto_now_add=True)

    class Meta:
        permissions = [
            ("create", "Can Create Posts"),
            ("read", "Can Read Posts"),
            ("edit", "Can Edit Posts"), 
        ]