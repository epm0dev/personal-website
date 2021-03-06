from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework.routers import DefaultRouter
from projects.views import ProjectViewSet, KeywordViewSet
from contact.views import ContactFormViewSet
from blog.views import PostViewSet
from feed.views import ActivityViewSet
from resume.views import ResumeViewSet


# Initialize a default router object and register API views with it
router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'keyword', KeywordViewSet, basename='keyword')
router.register(r'contact', ContactFormViewSet, basename='contact')
router.register(r'blog', PostViewSet, basename='blog')
router.register(r'feed', ActivityViewSet, basename='feed')
router.register(r'resume', ResumeViewSet, basename='resume')

# Define the Django applications URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='api/')),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
