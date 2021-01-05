from django.contrib import admin
from .models import ContactForm


# Register contact app models to the admin site
admin.site.register(ContactForm)
