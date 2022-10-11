from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

# from .managers import CustomUserManager, SubmitterManager, DeveloperManager, ManagerManager, AdminManager

class CustomUserManager(BaseUserManager):
    def save(self, *args, **kwargs):
        # If a new user, set the user's type base off base_type
        if not self.pk:
            self.type = self.base_type
        return super().save(*args,**kwargs)

class CustomUser(AbstractUser):
    class Types(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        MANAGER = "MANAGER", "Manager"
        DEVELOPER = "DEVELOPER", "Developer"
        SUBMITTER = "SUBMITTER", "Submitter"

    # model specific methods
    objects = CustomUserManager()

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
# MODEL MANAGERS
#############################################################################
class SubmitterManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=CustomUser.Types.SUBMITTER)

class DeveloperManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=CustomUser.Types.DEVELOPER)

class ManagerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=CustomUser.Types.MANAGER)

class AdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=CustomUser.Types.ADMIN)

#############################################################################
# PROXY MODELS 
#############################################################################
class Submitter(CustomUser):
    # User base_type is Submitter, but repeated here in case of change
    base_type = CustomUser.Types.SUBMITTER

    # model specific methods
    objects = SubmitterManager()

    class Meta:
        # prevents a table from being created for this model
        proxy = True

class Developer(CustomUser):
    base_type = CustomUser.Types.DEVELOPER

    # model specific methods
    objects = DeveloperManager()

    class Meta:
        # prevents a table from being created for this model
        proxy = True

class Manager(CustomUser):
    base_type = CustomUser.Types.MANAGER

    # model specific methods
    objects = ManagerManager()

    class Meta:
        # prevents a table from being created for this model
        proxy = True

class Admin(CustomUser):
    base_type = CustomUser.Types.ADMIN

    # model specific methods
    objects = AdminManager()

    class Meta:
        # prevents a table from being created for this model
        proxy = True