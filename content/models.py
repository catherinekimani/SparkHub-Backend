from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


CONTENT_TYPES = (
    ('text', 'Text'),
    ('image', 'Image'),
    ('video', 'Video'),
    ('link', 'Link')
)


class Content(models.Model):
    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=50, choices=CONTENT_TYPES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField(default="Write your comment here")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.content.title}"


class Like(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('content', 'user')