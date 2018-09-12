from django.urls import path
from . import views


app_name = 'board'
urlpatterns = [
    path('', views.post_list, name='list'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('write/', views.write, name='write'),
]