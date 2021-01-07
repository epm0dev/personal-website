from rest_framework import serializers
from .models import ProjectCreatedActivity, ProjectEditedActivity, PostCreatedActivity, PostEditedActivity


class ActivitySerializerBase(serializers.ModelSerializer):
    """
    An abstract serializer for feed activity models which defines additional behavior when converting activity objects
    to their serialized representation.
    """
    object_type = None

    def to_representation(self, instance):
        """
        A method which overrides the default serializer to_represtentation method to add a type field to the serialized
        representation of feed activity items. Each subclass of this abstract base class should specify the value to
        be stored with the type key as an attribute name object_type.
        """
        ret = super().to_representation(instance)
        ret['type'] = self.object_type
        return ret


class ProjectCreatedActivitySerializer(ActivitySerializerBase):
    """
    A serializer for the ProjectCreatedActivity model which includes most of its fields as well as its formatted
    date/time created properties.
    """
    object_type = 'project_created_activity'

    class Meta:
        model = ProjectCreatedActivity
        fields = ['pk', 'date_created', 'time_created', 'text', 'project']


class ProjectEditedActivitySerializer(ActivitySerializerBase):
    """
    A serializer for the ProjectEditedActivity model which includes most of its fields as well as its formatted
    date/time created properties.
    """
    object_type = 'project_edited_activity'

    class Meta:
        model = ProjectEditedActivity
        fields = ['pk', 'date_created', 'time_created', 'text', 'project']


class PostCreatedActivitySerializer(ActivitySerializerBase):
    """
    A serializer for the PostCreatedActivity model which includes most of its fields as well as its formatted
    date/time created properties.
    """
    object_type = 'post_created_activity'

    class Meta:
        model = PostCreatedActivity
        fields = ['pk', 'date_created', 'time_created', 'text', 'post']


class PostEditedActivitySerializer(ActivitySerializerBase):
    """
    A serializer for the PostEditedActivity model which includes most of its fields as well as its formatted
    date/time created properties.
    """
    object_type = 'post_edited_activity'

    class Meta:
        model = PostEditedActivity
        fields = ['pk', 'date_created', 'time_created', 'text', 'post']
