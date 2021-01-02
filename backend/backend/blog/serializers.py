from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    TODO Docs
    """

    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'contents', 'datetime_created', 'datetime_changed', 'project']
