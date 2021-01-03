from rest_framework import serializers
from .models import ProjectCreatedActivity, ProjectEditedActivity, PostCreatedActivity, PostEditedActivity


class ActivitySerializerBase(serializers.ModelSerializer):
    """
    TODO Docs
    """
    object_type = None

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['type'] = self.object_type
        return ret


class ProjectCreatedActivitySerializer(ActivitySerializerBase):
    """
    TODO Docs
    """
    object_type = 'project_created_activity'

    class Meta:
        model = ProjectCreatedActivity
        fields = ['datetime_created', 'text', 'project']


class ProjectEditedActivitySerializer(ActivitySerializerBase):
    """
    TODO Docs
    """
    object_type = 'project_edited_activity'

    class Meta:
        model = ProjectEditedActivity
        fields = ['datetime_created', 'text', 'project']


class PostCreatedActivitySerializer(ActivitySerializerBase):
    """
    TODO Docs
    """
    object_type = 'post_created_activity'

    class Meta:
        model = PostCreatedActivity
        fields = ['datetime_created', 'text', 'post']


class PostEditedActivitySerializer(ActivitySerializerBase):
    """
    TODO Docs
    """
    object_type = 'post_edited_activity'

    class Meta:
        model = PostEditedActivity
        fields = ['datetime_created', 'text', 'post']
