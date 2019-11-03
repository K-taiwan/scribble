from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('posts/', views.post_list),
    path('comments/', views.comment_list),
    path('posts/<int:pk>', views.post_detail, name='post_detail'),
    path('api/v1/posts/', views.api_posts),
    path('api/v1/comments/', views.api_comments),
]