from django.contrib import admin
from .models import DjangoUser, Company, Community, Project, Blog


admin.site.register(DjangoUser)
admin.site.register(Company)
admin.site.register(Community)
admin.site.register(Project)
admin.site.register(Blog)
