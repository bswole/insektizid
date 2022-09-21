from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class CustomUser(User):
    ROLES = ( 
        ('admin', 'Administrator'), # CRUD ALL
        ('manager', 'Manager'), # CRUD projects, (C)R(UD) users(developers, submitters), CRUD tickets(approval=>Done), CRUD comments
        ('lead', 'Team Lead'), # Developer with permission to review and approve tickets
        ('developer', 'Software Developer'), # (C)R(UD) tickets(authored_by, CR if project team member), comments(authored_by, CR if project team member)
        ('submitter', 'Ticket Submitter'), # (C)R(UD) tickets(authored_by, CR if project team member), (C)R(UD) comments(authored_by, CR if project team member)
    )

    username = None
    first_name = models.CharField(_("first name"), max_length=150, null=False)
    last_name = models.CharField(_("last name"), max_length=150, null=False)
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(_("password"), max_length=150, null=False)
    supervisor = ''

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        permissions = [
            # Users, CRUD: admin / CRUD: manager (dev, sub... if supervisor)
            # Projects, CRUD: admin, manager / R: dev, sub (if team member) 
            # Tickets, CRUD: admin / manager (if project team member) / dev (CR: if project team member, UD: if author) / 
        ]
        ordering = ["last_name", "first_name"]

    
    def __str__(self):
        return self.email