from django.contrib import admin
from .models import Project, Keyword


# Register projects app models to the admin site
admin.site.register(Project)
admin.site.register(Keyword)
