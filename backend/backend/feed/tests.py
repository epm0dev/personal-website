from django.test import TestCase
from .models import (
    ProjectCreatedActivity, ProjectEditedActivity, PostCreatedActivity, PostEditedActivity, ResumeUploadedActivity
)


class PostModelTestCase(TestCase):
    """
    TODO Docs
    """
    fixtures = ['feed-test.json']

    def test_create_project_created_activity(self):
        """
        TODO Docs
        """
        pass

    def test_create_project_edited_activity(self):
        """
        TODO Docs
        """
        pass

    def test_create_post_created_activity(self):
        """
        TODO Docs
        """
        pass

    def test_create_post_edited_activity(self):
        """
        TODO Docs
        """
        pass

    def test_create_resume_uploaded_activity(self):
        """
        TODO Docs
        """
        pass
