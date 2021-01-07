from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    A serializer for the Post model which includes most of its fields as well as its formatted date/time created and
    date/time changed properties.
    """
    class Meta:
        model = Post
        fields = [
            'pk', 'title', 'subtitle', 'contents', 'date_created', 'time_created', 'date_changed', 'time_changed',
            'project'
        ]
