from django.contrib import admin
from .models import Resume, ResumeSection, ResumeSubsection


# Register resume app models to the admin site
admin.site.register(Resume)
admin.site.register(ResumeSection)
admin.site.register(ResumeSubsection)
