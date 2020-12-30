from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    """
    TODO Docs
    """

    class Phase(models.IntegerChoices):
        """
        TODO Docs
        """

        DESIGN = 1, _('Design')
        IMPLEMENTATION = 2, _('Implementation')
        INTEGRATION = 3, _('Integration')
        MAINTENANCE = 4, _('Maintenance')

    class DisplayCategory(models.IntegerChoices):
        """
        TODO Docs
        """

        FEATURED = 1
        GENERAL = 2
        ARCHIVED = 3

    # Standard fields
    title = models.CharField(
        max_length=50,
        null=False,
        unique=True
    )
    description = models.TextField(
        max_length=500,
        null=False
    )
    description_verbose = models.TextField(
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
    phase = models.PositiveSmallIntegerField(
        choices=Phase.choices,
        default=Phase.DESIGN
    )
    display_category = models.PositiveIntegerField(
        choices=DisplayCategory.choices,
        default=DisplayCategory.GENERAL
    )

    # Relationship fields
    _keywords = models.ManyToManyField(
        'Keyword',
        related_name='projects'
    )

    class Meta:
        """
        TODO Docs
        """

        get_latest_by = 'datetime_created'
        ordering = ['phase', '-datetime_changed']
        unique_together = [
            ['description', 'description_verbose']
        ]


class Keyword(models.Model):
    """
    TODO Docs
    """

    # Standard fields
    word = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )

    # Relationship fields
    _projects = models.ManyToManyField(
        'Project',
        related_name='keywords'
    )

    class Meta:
        """
        TODO Docs
        """

        ordering = ['-word']
