from django.db import models
from projects.models import Project
from blog.models import Post
from resume.models import Resume


class ProjectActivityBase(models.Model):
    """
    An abstract model for feed activity relating to project objects.
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

    # Properties
    @property
    def date_created(self):
        """
        A property which returns the date when the activity was created, formatted for display.
        """
        return self.datetime_created.strftime('%m-%d-%Y')

    @property
    def time_created(self):
        """
        A property which returns the time when the activity was created, formatted for display.
        """
        return self.datetime_created.strftime('%H:%M:%S')

    class Meta:
        """
        A class which contains metadata for the project activity base class that specifies that the class is abstract
        as well as the field to order objects of its subclasses by.
        """
        abstract = True
        ordering = ['-datetime_created']


class ProjectCreatedActivity(ProjectActivityBase):
    """
    A model for feed activity that results from a new project object being created.
    """

    # Methods
    def __str__(self):
        """
        A method which defines the string representation of a project created activity object to contain the title of
        the new project as well as the date and time it was created.
        """
        return f'Created Project - {self.project.title} at {self.datetime_created.time()} on ' \
               f'{self.datetime_created.date()}'

    def save(self, *args, **kwargs):
        """
        A method which overrides the default model save method in order to set the project created activity object's
        text field to contain the title of the related project.
        """
        self.text = f'I created a new project titled {self.project.title}!'
        super(ProjectCreatedActivity, self).save(*args, **kwargs)


class ProjectEditedActivity(ProjectActivityBase):
    """
    A model for feed activity that results from an existing project object being edited.
    """

    # Methods
    def __str__(self):
        """
        A method which defines the string representation of a project edited activity object to contain the title of
        the project that was edited as well as the date and time it was edited.
        """
        return f'Edited Project - {self.project.title} at {self.datetime_created.time()} on ' \
               f'{self.datetime_created.date()}'

    def save(self, *args, **kwargs):
        """
        A method which overrides the default model save method in order to set the project edited activity object's
        text field to contain the title of the related project.
        """
        self.text = f'I edited my project titled {self.project.title}!'
        super(ProjectEditedActivity, self).save(*args, **kwargs)


class PostActivityBase(models.Model):
    """
    An abstract model for feed activity relating to post objects.
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
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='%(class)s_related'
    )

    # Properties
    @property
    def date_created(self):
        """
        A property which returns the date when the activity was created, formatted for display.
        """
        return self.datetime_created.strftime('%m-%d-%Y')

    @property
    def time_created(self):
        """
        A property which returns the time when the activity was created, formatted for display.
        """
        return self.datetime_created.strftime('%H:%M:%S')

    class Meta:
        """
        A class which contains metadata for the post activity base class that specifies that the class is abstract as
        well as the field to order objects of its subclasses by.
        """
        abstract = True
        ordering = ['-datetime_created']


class PostCreatedActivity(PostActivityBase):
    """
    A model for feed activity that results from a new post object being created.
    """

    # Methods
    def __str__(self):
        """
        A method which defines the string representation of a post created activity object to contain the title of the
        new post as well as the date and time it was created.
        """
        return f'Created Post - {self.post.title} at {self.datetime_created.time()} on {self.datetime_created.date()}'

    def save(self, *args, **kwargs):
        """
        A method which overrides the default model save method in order to set the post created activity object's text
        field to contain the title of the related post.
        """
        self.text = f'I created a new blog post titled {self.post.title}!'
        super(PostCreatedActivity, self).save(*args, **kwargs)


class PostEditedActivity(PostActivityBase):
    """
    A model for feed activity that results from an existing post object being edited.
    """

    # Methods
    def __str__(self):
        """
        A method which defines the string representation of a post edited activity object to contain the title of the
        post that was edited as well as the date and time it was edited.
        """
        return f'Edited Post - {self.post.title} at {self.datetime_created.time()} on {self.datetime_created.date()}'

    def save(self, *args, **kwargs):
        """
        A method which overrides the default model save method in order to set the post edited activity object's text
        field to contain the title of the related post.
        """
        self.text = f'I edited my blog post titled {self.post.title}!'
        super(PostEditedActivity, self).save(*args, **kwargs)


class ResumeUploadedActivity(models.Model):
    """
    A model for feed activity that results from a new resume object being created.
    """

    # Standard fields
    datetime_created = models.DateTimeField(
        auto_now_add=True
    )
    text = models.CharField(
        max_length=200,
        null=False,
        default='I uploaded a new version of my resume!'
    )

    # Relationships
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name='%(class)s_related'
    )

    # Properties
    @property
    def date_created(self):
        """
        A property which returns the date when the activity was created, formatted for display.
        """
        return self.datetime_created.strftime('%m-%d-%Y')

    @property
    def time_created(self):
        """
        A property which returns the time when the activity was created, formatted for display.
        """
        return self.datetime_created.strftime('%H:%M:%S')


    # Methods
    def __str__(self):
        """
        A method which defines the string representation of a resume uploaded activity object to contain the string
        representation of the resume new resume object.
        """
        return f'Resume Uploaded - {self.resume}'
