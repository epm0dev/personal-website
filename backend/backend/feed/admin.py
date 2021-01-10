from django.contrib import admin
from .models import (
    ProjectCreatedActivity, ProjectEditedActivity, PostCreatedActivity, PostEditedActivity, ResumeUploadedActivity
)


# Register feed app models to the admin site
admin.site.register(ProjectCreatedActivity)
admin.site.register(ProjectEditedActivity)
admin.site.register(PostCreatedActivity)
admin.site.register(PostEditedActivity)
admin.site.register(ResumeUploadedActivity)
