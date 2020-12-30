from django.test import TestCase
from models import (ProjectCreatedActivity, ProjectEditedActivity, PostCreatedActivity, PostEditedActivity,
                    GithubNewRepositoryActivity, GithubNewCommitActivity, LinkedinActivity)


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

    def test_create_github_new_repository_activity(self):
        """
        TODO Docs
        """
        pass

    def test_create_github_new_commit_activity(self):
        """
        TODO Docs
        """
        pass
