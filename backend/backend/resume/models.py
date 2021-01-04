from django.db import models


class ResumeOutline(models.Model):
    """
    TODO Docs
    """

    # Standard fields
    date_uploaded = models.DateField(auto_now_add=True)

    # Methods
    def __str__(self):
        return f'Resume Version: {self.date_uploaded.strftime("%m-%d-%Y")}'


class ResumeSection(models.Model):
    """
    TODO Docs
    """

    # Standard fields
    heading = models.CharField(
        max_length=50,
        null=False,
        default='Section Heading'
    )
    content = models.TextField(
        max_length=1000,
        null=False,
        default='Section content'
    )

    # Relationships
    outline = models.ForeignKey(
        ResumeOutline,
        related_name='sections',
        on_delete=models.CASCADE
    )

    # Methods
    def __str__(self):
        return f'"{self.heading}" section of {self.outline}'

    class Meta:
        """
        TODO Docs
        """

        ordering = ['pk']
