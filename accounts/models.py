from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class User(AbstractUser):
    class Types(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        MANAGER = "MANAGER", "Manager"
        DEVELOPER = "DEVELOPER", "Developer"
        SUBMITTER = "SUBMITTER", "Submitter"

    # default user role
    base_type = Types.SUBMITTER

    # user role
    type = models.CharField(
        _("Type"), 
        max_length=50, 
        choices=Types.choices,
        default=Types.SUBMITTER
    )
    # model specific methods
    # objects = CustomUserManager()

    def save(self, *args, **kwargs):
        # If a new user, set the user's type based off base_type if not already defined
        if not self.type or self.type == None:
            self.type = self.base_type
        return super().save(*args,**kwargs)

    # modify super() create_superuser method to assign admin type to superusers
    # ****** this code produces a superuser with User.Type.SUBMITTER not ADMIN as intended ******
    # def create_superuser(self, username, password, email=None):
    #     """
    #     Creates a super user with admin role.
    #     """
    #     user = super().create_superuser(self, username, password, email)
    #     user.type = User.Types.ADMIN
    #     user.save(using=self._db)
    #     return user


#############################################################################
# MODEL MANAGERS
#############################################################################
class SubmitterManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=User.Types.SUBMITTER)

class DeveloperManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=User.Types.DEVELOPER)

class ManagerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=User.Types.MANAGER)

class AdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=User.Types.ADMIN)

#############################################################################
# PROXY MODELS 
#############################################################################
class Submitter(User):
    # User base_type is Submitter, but repeated here in case of change
    base_type = User.Types.SUBMITTER

    # model specific methods
    objects = SubmitterManager()

    class Meta:
        # prevents a table from being created for this model
        proxy = True

class Developer(User):
    base_type = User.Types.DEVELOPER

    # model specific methods
    objects = DeveloperManager()

    class Meta:
        # prevents a table from being created for this model
        proxy = True

class Manager(User):
    base_type = User.Types.MANAGER

    # model specific methods
    objects = ManagerManager()

    class Meta:
        # prevents a table from being created for this model
        proxy = True

class Admin(User):
    base_type = User.Types.ADMIN

    # model specific methods
    objects = AdminManager()

    class Meta:
        # prevents a table from being created for this model
        proxy = True