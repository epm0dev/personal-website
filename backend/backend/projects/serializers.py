from rest_framework import serializers
from .models import Project, Keyword


class KeywordSerializer(serializers.ModelSerializer):
    """
    A serializer for the Keyword model which includes its pk and word fields.
    """
    class Meta:
        model = Keyword
        fields = ['pk', 'word']


class ProjectSerializer(serializers.ModelSerializer):
    """
    A serializer for the Project model for use when listing projects and, therefore, does not include all of each
    project object's details. It does, however, include each project object's related keywords and their phase and
    category properties.
    """
    keywords = KeywordSerializer(many=True, read_only=True)
    phase = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    @staticmethod
    def get_phase(obj):
        return obj.phase

    @staticmethod
    def get_category(obj):
        return obj.category

    class Meta:
        model = Project
        fields = ['pk', 'url', 'title', 'description', 'keywords', 'phase', 'category']


class ProjectDetailSerializer(serializers.ModelSerializer):
    """
    A serializer for the Project model for use when retrieving a single project object and, therefore, includes all of
    its details.
    """
    keywords = KeywordSerializer(many=True, read_only=True)
    phase = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    @staticmethod
    def get_phase(obj):
        return obj.phase

    @staticmethod
    def get_category(obj):
        return obj.category

    class Meta:
        model = Project
        fields = [
            'pk', 'url', 'title', 'description', 'description_verbose', 'date_created', 'time_created', 'date_changed',
            'time_changed', 'phase', 'category', 'keywords'
        ]
