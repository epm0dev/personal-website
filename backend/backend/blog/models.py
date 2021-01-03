from django.db import models
from projects.models import Project
import celery


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
        """
        TODO Docs
        """
        return f'{self.title} - {self.subtitle}'

    def save(self, *args, **kwargs):
        """
        TODO Docs
        """
        if self.pk:
            new_post = False
        else:
            new_post = True

        super(Post, self).save(*args, **kwargs)

        if new_post:
            celery.current_app.send_task('blog.tasks.new_post_created_activity', (self.pk,))
        else:
            celery.current_app.send_task('blog.tasks.new_post_edited_activity', (self.pk,))

    class Meta:
        """
        TODO Docs
        """

        get_latest_by = 'datetime_created'
        ordering = ['-datetime_created']
