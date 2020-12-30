from django.test import TestCase
from models import Project, Keyword


class ProjectModelTestCase(TestCase):
    """
    TODO Docs
    """

    fixtures = ['projects-test.json']

    def test_create_project(self):
        """
        TODO Docs
        """
        pass


class KeywordModelTestCase(TestCase):
    """
    TODO Docs
    """

    fixtures = ['projects-test.json']

    def test_create_keyword(self):
        """
        TODO Docs
        """
        pass
