from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth import get_user_model


# Create your models here.
class User(AbstractUser):
    email=models.EmailField(unique=True)

    groups = models.ManyToManyField(Group, related_name='musicapp_users')
    user_permissions = models.ManyToManyField(Permission, related_name='musicapp_users')

    def __str__(self):
        return self.email
    
User = get_user_model()

class MusicFile(models.Model):
    PUBLIC = 'public'
    PRIVATE = 'private'
    PROTECTED = 'protected'
    VISIBILITY_CHOICES = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
        (PROTECTED, 'Protected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='music_files/')
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES)
    allowed_emails = models.TextField(blank=True)

    def __str__(self):
        return self.title
    

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
