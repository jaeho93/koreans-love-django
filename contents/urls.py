from django.urls import path
from . import views

app_name = 'contents'
urlpatterns = [
    path('user/', views.user, name='user'),
    path('company/', views.company, name='company'),
    path('community/', views.community, name='community'),
    path('project/', views.project, name='project'),
    path('archive/', views.archive, name='archive'),
]