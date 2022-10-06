from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class SubmitterManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=UserModel.Types.SUBMITTER)

class DeveloperManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=UserModel.Types.DEVELOPER)

class ManagerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=UserModel.Types.MANAGER)

class AdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=UserModel.Types.ADMIN)
