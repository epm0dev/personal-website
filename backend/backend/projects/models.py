from django.db import models
from django.utils.translation import gettext_lazy as _
import celery


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

    FEATURED = 1, _('Featured')
    GENERAL = 2, _('General')
    ARCHIVED = 3, _('Archived')


class FeaturedProjectManager(models.Manager):
    """
    TODO Docs
    """

    def get_queryset(self):
        """
        TODO Docs
        """
        return super().get_queryset().filter(_category=DisplayCategory.FEATURED)


class GeneralProjectManager(models.Manager):
    """
    TODO Docs
    """

    def get_queryset(self):
        """
        TODO Docs
        """
        return super().get_queryset().filter(_category=DisplayCategory.GENERAL)


class ArchivedProjectManager(models.Manager):
    """
    TODO Docs
    """

    def get_queryset(self):
        """
        TODO Docs
        """
        return super().get_queryset().filter(_category=DisplayCategory.ARCHIVED)


class Project(models.Model):
    """
    TODO Docs
    """

    # Project object managers
    objects = models.Manager()
    featured = FeaturedProjectManager()
    general = GeneralProjectManager()
    archived = ArchivedProjectManager()

    # Standard fields
    title = models.CharField(
        max_length=50,
        null=False,
        unique=True
    )
    description = models.TextField(
        max_length=500,
        null=False,
        default='A short-form description for this project has yet to be added.'
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
    _phase = models.PositiveSmallIntegerField(
        choices=Phase.choices,
        default=Phase.DESIGN
    )
    _category = models.PositiveIntegerField(
        choices=DisplayCategory.choices,
        default=DisplayCategory.GENERAL
    )

    # Relationship fields
    _keywords = models.ManyToManyField(
        'Keyword',
        related_name='projects',
        blank=True
    )

    # Properties
    @property
    def phase(self):
        return Phase(self._phase).label

    @property
    def category(self):
        return DisplayCategory(self._category).label

    @property
    def date_created(self):
        return self.datetime_created.strftime('%m-%d-%Y')

    @property
    def time_created(self):
        return self.datetime_created.strftime('%H:%M:%S')

    @property
    def date_changed(self):
        return self.datetime_changed.strftime('%m-%d-%Y')

    @property
    def time_changed(self):
        return self.datetime_changed.strftime('%H:%M:%S')

    # Methods
    def __str__(self):
        """
        TODO Docs
        """
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            newProject = False
        else:
            newProject = True

        super(Project, self).save(*args, **kwargs)

        if newProject:
            celery.current_app.send_task('projects.tasks.new_project_created_activity', (self.pk,))
        else:
            celery.current_app.send_task('projects.tasks.new_project_edited_activity', (self.pk,))


    class Meta:
        """
        TODO Docs
        """

        get_latest_by = 'datetime_created'
        ordering = ['_phase', '-datetime_changed']
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
        related_name='keywords',
        blank=True
    )

    # Methods
    def __str__(self):
        """
        TODO Docs
        """
        return self.word

    class Meta:
        """
        TODO Docs
        """

        ordering = ['word']
