from rest_framework import serializers
from .models import ResumeOutline


class ResumeOutlineSerializer(serializers.ModelSerializer):
    """
    TODO Docs
    """

    class Meta:
        model = ResumeOutline
        fields = []