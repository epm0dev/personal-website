from django.contrib import admin
from .models import ProjectCreatedActivity, ProjectEditedActivity, PostCreatedActivity, PostEditedActivity


admin.site.register(ProjectCreatedActivity)
admin.site.register(ProjectEditedActivity)
admin.site.register(PostCreatedActivity)
admin.site.register(PostEditedActivity)
