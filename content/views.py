from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import Content, Comment, Like

from .serializers import ContentSerializer, CommentSerializer, LikeSerializer

from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([AllowAny])
def content_list_view(request):
    contents = Content.objects.all()
    serializer = ContentSerializer(contents, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_content_view(request):
    serializer = ContentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def content_list_view(request):
    contents = Content.objects.all()
    serializer = ContentSerializer(contents, many=True)
    return Response(serializer.data)
@api_view(['GET'])
@permission_classes([AllowAny])
def list_comments_view(request, pk):
    content = get_object_or_404(Content, pk=pk)
    comments = content.comment_set.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment_view(request, pk):
    content = get_object_or_404(Content, pk=pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(content=content, author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_view(request, pk):
    content = get_object_or_404(Content, pk=pk)
    user = request.user
    already_liked = Like.objects.filter(content=content, user=user).exists()
    if already_liked:
        Like.objects.filter(content=content, user=user).delete()
        message = 'Content unliked'
    else:
        Like.objects.create(content=content, user=user)
        message = 'Content liked'
    return Response({'message': message}, status=status.HTTP_200_OK)
