from django.db import models


class ActivityBase(models.Model):
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

    class Meta:
        """
        TODO Docs
        """
        abstract = True
        ordering = ['-datetime_created']


class ProjectActivityBase(ActivityBase):
    """
    TODO Docs
    """
    pass


class ProjectCreatedActivity(ProjectActivityBase):
    """
    TODO Docs
    """
    pass


class ProjectEditedActivity(ProjectActivityBase):
    """
    TODO Docs
    """
    pass


class PostActivityBase(ActivityBase):
    """
    TODO Docs
    """
    pass


class PostCreatedActivity(PostActivityBase):
    """
    TODO Docs
    """
    pass


class PostEditedActivity(PostActivityBase):
    """
    TODO Docs
    """
    pass


class GithubActivityBase(ProjectActivityBase):
    """
    TODO Docs
    """
    pass


class GithubNewRepositoryActivity(GithubActivityBase):
    """
    TODO Docs
    """
    pass


class GithubNewCommitActivity(GithubActivityBase):
    """
    TODO Docs
    """
    pass


class LinkedinActivity(ActivityBase):
    """
    TODO Docs
    """
    pass
