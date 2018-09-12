from django.urls import path
from . import views


app_name = 'board'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('write/', views.post_write, name='post_write'),
]