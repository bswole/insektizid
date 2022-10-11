# from django.contrib.auth.models import BaseUserManager
# from django.contrib.auth import get_user_model

# UserModel = get_user_model() 

# ******************************************************************
# having an issue making migrations when managers are in this file.
# ******************************************************************

# class CustomUserManager(BaseUserManager):
#     def save(self, *args, **kwargs):
#         # If a new user, set the user's type base off base_type
#         if not self.pk:
#             self.type = self.base_type
#         return super().save(*args,**kwargs)

# class SubmitterManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(type=UserModel.Types.SUBMITTER)

# class DeveloperManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(type=UserModel.Types.DEVELOPER)

# class ManagerManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(type=UserModel.Types.MANAGER)

# class AdminManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(type=UserModel.Types.ADMIN)
