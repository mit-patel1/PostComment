from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('add_post/', views.add_post, name='add_post'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
]
