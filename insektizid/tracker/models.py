from django.conf import settings
from django.db import models

from .managers import TimeStampedModelManager, ProjectManager, TicketManager, CommentManager, AttachmentManager

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    objects = TimeStampedModelManager

    class Meta:
        abstract = True

class Project(TimeStampedModel):
    title = models.CharField(max_length=150)
    team_members = models.ManyToManyField(settings.AUTH_USER_MODEL)
    # manager stored in author

    objects = ProjectManager

    class Meta:
        ordering = ['title']

class Ticket(TimeStampedModel):
    STATUSES = (
        ('BACKLOG','Backlog'),
        ('TODO','Todo'),
        ('INPROGRESS','In Progress'),
        ('REVIEW','Review'),
        ('DONE','Done'),
    )
    LABELS = (
        ('ENHANCEMENT','enhancement'),
        ('BUG','bug'),
        ('DOCUMENTATION','documentation'),
        ('DUPLICATE','duplicate'),
        # ('GOODFIRSTISSUE','good first issue'),
        ('HELPWANTED','help wanted'),
        ('INVALID','invalid'),
        ('QUESTION','question'),
        ('WONTFIX','wontfix'),
        ('UNASSIGNED','unassigned'),
    )
    PRIORITIES = (
        ('H','High'),
        ('M','Medium'),
        ('L','Low'),
    )
    
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING) # TODO on delete set to project manager
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUSES)
    priority = models.CharField(max_length=50, choices=PRIORITIES)
    # labels = models.CharField(max_length=1, choices=LABELS) # TODO enable adding labels from limited list above
    deadline = models.DateField()

    objects = TicketManager

    # class Meta:
        # ordering = ['project']

class Comment(TimeStampedModel):
    message = models.TextField(max_length=150)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    objects = CommentManager

class Attachment(TimeStampedModel):
    file_url = models.CharField(max_length=255)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    objects = AttachmentManager