from django.contrib import admin
from django.urls import include, path
from . import views
from contents.views import user_list

urlpatterns = [
    path('', user_list),
    path('admin/', admin.site.urls),
    path('acounts/', include('accounts.urls')),
    path('board/', include('board.urls')),
    path('contents/', include('contents.urls')),
    path('info/', views.site_info),
]
