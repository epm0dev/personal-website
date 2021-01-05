from django.contrib import admin
from .models import ResumeOutline, ResumeSection


# Register resume app models to the admin site
admin.site.register(ResumeOutline)
admin.site.register(ResumeSection)
