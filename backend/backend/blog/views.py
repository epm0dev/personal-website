from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing and retrieving blog posts.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()
