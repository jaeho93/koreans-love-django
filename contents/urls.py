from django.urls import path
from . import views

app_name = 'contents'
urlpatterns = [
    path('user/', views.user_list, name='user_list'),
    path('company/', views.company_list, name='company_list'),
    path('community/', views.community_list, name='community_list'),
    path('project/', views.project_list, name='project_list'),
    path('blog/', views.blog_list, name='blog_list'),
]
