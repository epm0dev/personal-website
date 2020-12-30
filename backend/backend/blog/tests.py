from django.test import TestCase
from models import Post


class PostModelTestCase(TestCase):
    """
    TODO Docs
    """

    fixtures = ['blog-test.json']

    def test_create_post(self):
        """
        TODO Docs
        """
        pass
