from django.contrib import admin
from django.urls import include, path
from . import views
import contents


urlpatterns = [
    path('', contents.views.user),
    path('admin/', admin.site.urls),
    path('acounts/', include('accounts.urls')),
    path('board/', include('board.urls')),
    path('contents/', include('contents.urls')),
    path('info/', views.info),
]
