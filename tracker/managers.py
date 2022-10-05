from django.conf import settings
from django.db import models

class TimeStampedModelManager(models.Manager):
    pass

class ProjectManager(TimeStampedModelManager):

    def create_project(self, user: settings.AUTH_USER_MODEL):
        project = self.model(user=user)
        return project

class TicketManager(TimeStampedModelManager):

    def create_ticket(self, user: settings.AUTH_USER_MODEL):
        ticket = self.model(user=user)
        return ticket


class CommentManager(TimeStampedModelManager):

    def create_comment(self, user: settings.AUTH_USER_MODEL):
        comment = self.model(user=user)
        return comment

class AttachmentManager(TimeStampedModelManager):

    def create_attachment(self, user: settings.AUTH_USER_MODEL):
        attachment = self.model(user=user)
        return attachment
