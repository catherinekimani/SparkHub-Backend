from rest_framework import serializers
from .models import Content, Category, Comment, Like

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):
    content_type = serializers.CharField(source='get_content_type_display')
    categories = CategorySerializer(many=True, read_only=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Content
        fields = (
            'id', 'title', 'content_type', 'categories', 'author', 'created_at', 'updated_at'
        )

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ('id', 'content', 'author', 'created_at')


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('id', 'user', 'created_at')