from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework.routers import DefaultRouter
from projects.views import ProjectViewSet
from contact.views import ContactFormViewSet


router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'contact', ContactFormViewSet, basename='contact')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='api/')),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
