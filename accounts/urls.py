from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in'),
    path('profile/', views.user_profile, name='profile'),
    path('delete/', views.user_delete, name='delete'),
]