from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in'),
    path('profile/', views.profile, name='profile'),
    path('delete/', views.delete, name='delete'),
]