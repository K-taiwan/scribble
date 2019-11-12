from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('posts/new/', views.post_create, name='post_create'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('posts/<int:pk>/comments/<int:comment_pk>/edit/', views.comment_edit, name='comment_edit'),
    path('posts/<int:pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name="comment_delete"),
    path('posts/<int:pk>/comments/new/', views.comment_create, name='comment_create'),
    path('comments/', views.comment_list),
    path('api/v1/posts/', views.api_posts)
]