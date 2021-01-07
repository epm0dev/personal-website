from django.db import models
from projects.models import Project
import celery


class Post(models.Model):
    """
    A model for blog posts. Blog post objects have a title, subtitle, text content, date & time created, date & time
    edited, and a related project object, if any.
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

    # Properties
    @property
    def date_created(self):
        """
        A property which returns the date when a blog post was created, formatted for display.
        """
        return self.datetime_created.strftime('%m-%d-%Y')

    @property
    def time_created(self):
        """
        A property which returns the time when a blog post was created, formatted for display.
        """
        return self.datetime_created.strftime('%H:%M:%S')

    @property
    def date_changed(self):
        """
        A property which returns the date when a blog post was last edited, formatted for display.
        """
        return self.datetime_created.strftime('%m-%d-%Y')

    @property
    def time_changed(self):
        """
        A property which returns the date when a blog post was last edited, formatted for display.
        """
        return self.datetime_created.strftime('%H:%M:%S')

    # Methods
    def __str__(self):
        """
        A method which defines the string representation of a blog post object to contain its title and subtitle,
        separated by a hyphen.
        """
        return f'{self.title} - {self.subtitle}'

    def save(self, *args, **kwargs):
        """
        A method which overrides the default model save method in order to schedule celery tasks when a blog post is
        created or edited.
        """
        # If the blog post object has a primary key, then it has already been created, otherwise it has not
        if self.pk:
            new_post = False
        else:
            new_post = True

        # Call the superclass' save method to save the post to the database
        super(Post, self).save(*args, **kwargs)

        # Schedule a celery task corresponding to whether the post object was created or edited
        if new_post:
            celery.current_app.send_task('blog.tasks.new_post_created_activity', (self.pk,))
        else:
            celery.current_app.send_task('blog.tasks.new_post_edited_activity', (self.pk,))

    class Meta:
        """
        A class which contains metadata for the post class that defines the field to determine the latest post from and
        the field to order posts by.
        """
        get_latest_by = 'datetime_created'
        ordering = ['-datetime_created']
