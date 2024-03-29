from django.contrib import admin
from .models import Category, Content, Comment, Like

admin.site.register(Content)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Comment)