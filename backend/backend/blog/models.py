from django.db import models
from projects.models import Project


class Post(models.Model):
    """
    TODO Docs
    """

    # Standard fields
    title = models.CharField(
        max_length=100,
        null=False
    )
    contents = models.TextField(
        max_length=10000,
        null=False,
        default='A long-form description for this project has yet to be added.'
    )
    datetime_created = models.DateTimeField(
        auto_now_add=True
    )
    datetime_changed = models.DateTimeField(
        auto_now=True
    )

    # Relationship fields
    project = models.ForeignKey(
        Project,
        related_name='projects',
        on_delete=models.CASCADE
    )

    class Meta:
        """
        TODO Docs
        """

        get_latest_by = 'datetime_created'
        ordering = ['-datetime_created']
