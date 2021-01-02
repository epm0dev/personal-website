from rest_framework import serializers
from .models import Project, Keyword


class KeywordSerializer(serializers.ModelSerializer):
    """
    TODO Docs
    """

    class Meta:
        model = Keyword
        fields = ['pk', 'word']


class ProjectSerializer(serializers.ModelSerializer):
    """
    TODO Docs
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
    TODO Docs
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
            'pk', 'url', 'title', 'description', 'description_verbose', 'datetime_created', 'datetime_changed', 'phase',
            'category', 'keywords'
        ]
