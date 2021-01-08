from django.db import models


class ResumeOutline(models.Model):
    """
    A model for resume outlines. Resume outline objects only contain the date they were uploaded.
    """

    # Standard fields
    date_uploaded = models.DateField(auto_now_add=True)

    # Methods
    def __str__(self):
        """
        A method which defines the string representation of a resume outline object to contain the date when it was
        uploaded.
        """
        return f'Resume Version: {self.date_uploaded.strftime("%m-%d-%Y")}'

    class Meta:
        """
        A class which contains metadata for the resume outline class that defines the field to determine the latest
        resume outline from.
        """
        get_latest_by = ['date_uploaded']


class ResumeSection(models.Model):
    """
    A model for sections of a resume outline. Resume section objects contain a heading, their content and the resume
    outline object that they are related to.
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
        """
        A method which defines the string representation of a resume section object to contain the its heading as well
        as the string representation of its related resume outline object.
        """
        return f'"{self.heading}" section of {self.outline}'

    class Meta:
        """
        A class which contains metadata for the resume section class that specifies that resume section objects should
        be ordered by ascending primary key, or, in other words, the order in which they were created.
        """
        ordering = ['pk']
