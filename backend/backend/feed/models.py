from django.db import models
from projects.models import Project
from blog.models import Post


class ProjectActivityBase(models.Model):
    """
    TODO Docs
    """

    # Standard fields
    datetime_created = models.DateTimeField(
        auto_now_add=True
    )
    text = models.CharField(
        max_length=200,
        null=False
    )

    # Relationships
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_related'
    )

    class Meta:
        abstract = True
        ordering = ['-datetime_created']


class ProjectCreatedActivity(ProjectActivityBase):
    """
    TODO Docs
    """

    # Methods
    def __str__(self):
        return f'Created Project - {self.project.title} at {self.datetime_created.time()} on {self.datetime_created.date()}'

    def save(self, *args, **kwargs):
        self.text = f'I created a new project titled {self.project.title}!'
        super(ProjectCreatedActivity, self).save(*args, **kwargs)



class ProjectEditedActivity(ProjectActivityBase):
    """
    TODO Docs
    """

    # Methods
    def __str__(self):
        return f'Edited Project - {self.project.title} at {self.datetime_created.time()} on {self.datetime_created.date()}'

    def save(self, *args, **kwargs):
        self.text = f'I edited my project titled {self.project.title}!'
        super(ProjectEditedActivity, self).save(*args, **kwargs)


class PostActivityBase(models.Model):
    """
    TODO Docs
    """

    # Standard fields
    datetime_created = models.DateTimeField(
        auto_now_add=True
    )
    text = models.CharField(
        max_length=200,
        null=False
    )

    # Relationships
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='%(class)s_related'
    )

    class Meta:
        abstract = True
        ordering = ['-datetime_created']


class PostCreatedActivity(PostActivityBase):
    """
    TODO Docs
    """

    def save(self, *args, **kwargs):
        self.text = f'I created a new blog post titled {self.project.title}!'
        super(ProjectCreatedActivity, self).save(*args, **kwargs)


class PostEditedActivity(PostActivityBase):
    """
    TODO Docs
    """

    def save(self, *args, **kwargs):
        self.text = f'I edited my blog post titled {self.project.title}!'
        super(ProjectCreatedActivity, self).save(*args, **kwargs)
