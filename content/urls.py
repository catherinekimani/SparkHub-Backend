from django.urls import path
from .views import (
    content_list_view,
    create_content_view,
    list_comments_view,
    create_comment_view,
    like_view,
)

urlpatterns = [
    path('', content_list_view, name='content-list'),
    path('create/', create_content_view, name='create-content'),
    path('content/', content_list_view, name='content-list'),

    path('<int:pk>/comments/', list_comments_view, name='list-comments'),
    path('<int:pk>/comments/create/', create_comment_view, name='create-comment'),

    path('<int:pk>/like/', like_view, name='like-content'),
]
