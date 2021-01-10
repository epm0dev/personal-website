from rest_framework import serializers
from .models import Resume, ResumeSection, ResumeSubsection


class ResumeSubsectionSerializer(serializers.ModelSerializer):
    """
    A serializer for the ResumeSubsection model which includes its pk, heading, subtext and paragraphs fields.
    """
    class Meta:
        model = ResumeSubsection
        fields = ['pk', 'heading', 'subtext', 'paragraphs']


class ResumeSectionSerializer(serializers.ModelSerializer):
    """
    A serializer for the ResumeSection model which includes its pk, heading, and paragraphs fields, as well as a nested
    list of all of a resume section's related resume subsection objects, serialized.
    """
    subsections = ResumeSubsectionSerializer(many=True, read_only=True)

    class Meta:
        model = ResumeSection
        fields = ['pk', 'heading', 'paragraphs', 'subsections']


class ResumeSerializer(serializers.ModelSerializer):
    """
    A serializer for the Resume model which includes its pk, date_uploaded and time_uploaded fields, as well as a nested
    list of all of a resume's related resume section objects, serialized.
    """
    sections = ResumeSectionSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = ['pk', 'date_uploaded', 'time_uploaded', 'sections']
