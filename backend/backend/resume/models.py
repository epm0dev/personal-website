from django.db import models
from django.dispatch import receiver
from json import JSONEncoder
from typing import Any
import celery


class ParagraphJSONEncoder(JSONEncoder):
    """
    TODO Docs
    """

    def encode(self, o: Any) -> str:
        """
        TODO Docs
        """
        if not isinstance(o, list):
            raise TypeError(f'Expected type list, but recieved type {type(o)}')
        return super().encode(o)


class Resume(models.Model):
    """
    TODO Docs
    """

    # Standard fields
    document = models.FileField(
        upload_to='resume/'
    )
    pdf = models.FileField(
        upload_to='resume/'
    )
    date_uploaded = models.DateField(
        auto_now_add=True
    )
    time_uploaded = models.TimeField(
        auto_now_add=True
    )

    # Methods
    def __str__(self):
        """
        A method which defines the string representation of a resume object to contain the date when it was uploaded.
        """
        return f'Resume Version: {self.date_uploaded.strftime("%m-%d-%Y")}'

    def save(self, *args, **kwargs):
        """
        A method which overrides the default model save method in order to schedule a celery task when a new resume is
        created.
        """
        # If the resume object has a primary key, then it has already been created, otherwise it has not
        if self.pk:
            new_project = False
        else:
            new_project = True

        # Call the superclass' save method to save the resume to the database
        super(Resume, self).save(*args, **kwargs)

        # Schedule a celery task if the resume object was just created
        if new_project:
            celery.current_app.send_task('resume.tasks.new_resume_uploaded_activity', args=(self.pk,), countdown=5.)

    class Meta:
        """
        A class which contains metadata for the resume class that defines the field to determine the latest resume
        object from.
        """
        get_latest_by = ['date_uploaded', 'time_uploaded']


class ResumeSectionBase(models.Model):
    """
    TODO Docs
    """

    # Standard fields
    heading = models.CharField(
        max_length=500,
        null=False,
        default='Section Heading'
    )
    paragraphs = models.JSONField(
        encoder=ParagraphJSONEncoder,
        default=list
    )

    class Meta:
        """
        TODO Docs
        """
        abstract = True
        ordering = ['pk']


class ResumeSection(ResumeSectionBase):
    """
    TODO Docs
    """

    # Relationships
    resume = models.ForeignKey(
        Resume,
        related_name='sections',
        on_delete=models.CASCADE,
        null=True
    )

    # Methods
    def __str__(self):
        """
        TODO Docs
        """
        return f'{self.heading} Section; {self.resume}'


class ResumeSubsection(ResumeSectionBase):
    """
    TODO Docs
    """

    # Standard fields
    subtext = models.CharField(
        max_length=500,
        null=True
    )

    # Relationships
    section = models.ForeignKey(
        ResumeSection,
        related_name='subsections',
        on_delete=models.CASCADE,
        null=True
    )

    # Methods
    def __str__(self):
        """
        TODO Docs
        """
        return f'{self.heading} Subsection; {self.section}'


@receiver(models.signals.post_save, sender=Resume)
def create_resume(sender, instance, created, **kwargs):
    """
    TODO Docs
    """
    from .scripts import Resume

    if created:
        resume = Resume(instance.document.path)
        for s in resume.sections:
            if len(s.subsections) > 0:
                section = ResumeSection(
                    heading=s.heading,
                    resume=instance
                )
                section.save()

                for sub in s.subsections:
                    subsection = ResumeSubsection(
                        heading=sub.heading,
                        subtext=sub.subtext,
                        paragraphs=sub.paragraphs,
                        section=section
                    )
                    subsection.save()
            else:
                section = ResumeSection(
                    heading=s.heading,
                    paragraphs=s.paragraphs,
                    resume=instance
                )
                section.save()
