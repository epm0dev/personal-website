from rest_framework import serializers
from .models import ResumeOutline, ResumeSection


class ResumeSectionSerializer(serializers.ModelSerializer):
    """
    A serializer for the ResumeSection model which includes its pk, heading and content fields.
    """
    class Meta:
        model = ResumeSection
        fields = ['pk', 'heading', 'content']


class ResumeOutlineSerializer(serializers.ModelSerializer):
    """
    A serializer for the ResumeOutline model which includes its pk and date_uploaded fields, as well as a nested list of
    all of an outline's related resume section objects, serialized.
    """
    sections = ResumeSectionSerializer(many=True, read_only=True)

    class Meta:
        model = ResumeOutline
        fields = ['pk', 'date_uploaded', 'sections']
