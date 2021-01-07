from rest_framework import serializers
from .models import ResumeOutline, ResumeSection


class ResumeSectionSerializer(serializers.ModelSerializer):
    """
    TODO Docs
    """
    class Meta:
        model = ResumeSection
        fields = []


class ResumeOutlineSerializer(serializers.ModelSerializer):
    """
    TODO Docs
    """
    sections = ResumeSectionSerializer(many=True, read_only=True)

    class Meta:
        model = ResumeOutline
        fields = []
