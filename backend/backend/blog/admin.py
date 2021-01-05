from django.contrib import admin
from .models import Post


# Register blog app models to the admin site
admin.site.register(Post)
