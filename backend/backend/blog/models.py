from django.db import models
from projects.models import Project


class Post(models.Model):
    """
    TODO Docs
    """

    # Standard fields
    title = models.CharField(
        max_length=100,
        null=False,
        default='Post Title'
    )
    subtitle = models.CharField(
        max_length=200,
        null=False,
        default='Post Subtitle'
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
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    # Methods
    def __str__(self):
        return f'{self.title} - {self.subtitle}'

    class Meta:
        """
        TODO Docs
        """

        get_latest_by = 'datetime_created'
        ordering = ['-datetime_created']
