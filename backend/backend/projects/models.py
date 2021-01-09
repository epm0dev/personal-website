from django.db import models
from django.utils.translation import gettext_lazy as _
import celery


class Phase(models.IntegerChoices):
    """
    A class which defines the different stages that a project object can be in, as well as their string representations.
    """
    DESIGN = 1, _('Design')
    IMPLEMENTATION = 2, _('Implementation')
    INTEGRATION = 3, _('Integration')
    MAINTENANCE = 4, _('Maintenance')


class DisplayCategory(models.IntegerChoices):
    """
    A class which defines the different display categories that a project object can have, as well as their string
    representations.
    """
    FEATURED = 1, _('Featured')
    GENERAL = 2, _('General')
    ARCHIVED = 3, _('Archived')


class FeaturedProjectManager(models.Manager):
    """
    A custom manager for project objects whose queryset contains only projects of the 'Featured' display category.
    """
    def get_queryset(self):
        """
        A method which overrides the default manager get_queryset method to filter project objects by display category
        to returns only those of the 'Featured' display category.
        """
        return super().get_queryset().filter(_category=DisplayCategory.FEATURED)


class GeneralProjectManager(models.Manager):
    """
    A custom manager for project objects whose queryset contains only projects of the 'General' display category.
    """
    def get_queryset(self):
        """
        A method which overrides the default manager get_queryset method to filter project objects by display category
        to returns only those of the 'General' display category.
        """
        return super().get_queryset().filter(_category=DisplayCategory.GENERAL)


class ArchivedProjectManager(models.Manager):
    """
    A custom manager for project objects whose queryset contains only projects of the 'Archived' display category.
    """
    def get_queryset(self):
        """
        A method which overrides the default manager get_queryset method to filter project objects by display category
        to returns only those of the 'Archived' display category.
        """
        return super().get_queryset().filter(_category=DisplayCategory.ARCHIVED)


class Project(models.Model):
    """
    A model for projects. Project objects have a title, description, verbose description, date & time created, date &
    time edited, a phase, a display category and related keyword objects, if any.
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
        """
        A property which returns the string representation of a project objects private phase attribute.
        """
        return Phase(self._phase).label

    @property
    def category(self):
        """
        A property which returns the string representation of a project objects private category attribute.
        """
        return DisplayCategory(self._category).label

    @property
    def date_created(self):
        """
        A property which returns the date when the project was created, formatted for display.
        """
        return self.datetime_created.strftime('%m-%d-%Y')

    @property
    def time_created(self):
        """
        A property which returns the time when the project was created, formatted for display.
        """
        return self.datetime_created.strftime('%H:%M:%S')

    @property
    def date_changed(self):
        """
        A property which returns the date when the project was edited, formatted for display.
        """
        return self.datetime_changed.strftime('%m-%d-%Y')

    @property
    def time_changed(self):
        """
        A property which returns the time when the project was edited, formatted for display.
        """
        return self.datetime_changed.strftime('%H:%M:%S')

    # Methods
    def __str__(self):
        """
        A method which defines the string representation of a project object to contain its title.
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        A method which overrides the default model save method in order to schedule celery tasks when a project is
        created or edited.
        """
        # If the project object has a primary key, then it has already been created, otherwise it has not
        if self.pk:
            newProject = False
        else:
            newProject = True

        # Call the superclass' save method to save the project to the database
        super(Project, self).save(*args, **kwargs)

        # Schedule a celery task corresponding to whether the project object was created or edited
        if newProject:
            celery.current_app.send_task('projects.tasks.new_project_created_activity', args=(self.pk,), countdown=5.)
        else:
            celery.current_app.send_task('projects.tasks.new_project_edited_activity', args=(self.pk,), countdown=5.)

    class Meta:
        """
        A class which contains metadata for the project class that defines the field to determine the latest project
        from, the fields to order projects by and fields that should be unique together.
        """
        get_latest_by = 'datetime_created'
        ordering = ['_phase', '-datetime_changed']
        unique_together = [
            ['description', 'description_verbose']
        ]


class Keyword(models.Model):
    """
    A model for keywords which pertain to a project. Keyword objects contain the word itself and any number of related
    project objects.
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
        A method which defines the string representation of a keyword object to contain the word itself.
        """
        return self.word

    class Meta:
        """
        A class which contains metadata for the project class that specifies that keyword objects should be ordered
        alphabetically.
        """
        ordering = ['word']
