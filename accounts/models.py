from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from . import managers


class User(AbstractUser):
    class Types(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        MANAGER = "MANAGER", "Manager"
        DEVELOPER = "DEVELOPER", "Developer"
        SUBMITTER = "SUBMITTER", "Submitter"

    # model specific methods
    objects = managers.UserManager()

    # default user role
    base_type = Types.SUBMITTER

    # user role
    type = models.CharField(
        _("Type"), 
        max_length=50, 
        choices=Types.choices,
        default=Types.SUBMITTER
    )

#############################################################################
# PROXY MODELS 
#############################################################################
class Submitter(User):
    # User base_type is Submitter, but repeated here in case of change
    base_type = User.Types.SUBMITTER

    # model specific methods
    objects = managers.SubmitterManager()

    class Meta:
        # prevents a table from being created for this model
        proxy = True

class Developer(User):
    base_type = User.Types.DEVELOPER

    # model specific methods
    objects = managers.DeveloperManager()

    class Meta:
        # prevents a table from being created for this model
        proxy = True

class Manager(User):
    base_type = User.Types.MANAGER

    # model specific methods
    objects = managers.ManagerManager()

    class Meta:
        # prevents a table from being created for this model
        proxy = True

class Admin(User):
    base_type = User.Types.ADMIN

    # model specific methods
    objects = managers.AdminManager()

    class Meta:
        # prevents a table from being created for this model
        proxy = True