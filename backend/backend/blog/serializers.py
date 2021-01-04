from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    TODO Docs
    """

    class Meta:
        model = Post
        fields = [
            'pk', 'title', 'subtitle', 'contents', 'date_created', 'time_created', 'date_changed', 'time_changed',
            'project'
        ]
