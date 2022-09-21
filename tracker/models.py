# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class Roles(Permission):
#     pass

# class CustomUser(AbstractUser):
#     pass

#     def __str__(self):
#         return self.username


    # ROLES = (
    #     ('A','Admin'),
    #     ('M','Manager'),
    #     ('D','Developer'),
    #     ('S','Submitter'),
    # )

    # first_name = models.CharField(max_length=30) 
    # last_name = models.CharField(max_length=30) 
    # email = models.EmailField() 
    # password = models.CharField()
    # role = models.CharField(max_length=1, choices=ROLES)

# class BaseModel(models.Model):
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     authored_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL)

# class Attachment(BaseModel):
#     file_url = ''

# class Project(BaseModel):
#     title = ''
#     team_members = ''

# class Ticket(BaseModel):
#     STATUSES = (
#         ('B','Backlog'),
#         ('T','Todo'),
#         ('I','In Progress'),
#         ('R','Review'),
#         ('D','Done'),
#     )
#     LABELS = (
#         ('e','enhancement'),
#         ('b','bug'),
#         ('d','documentation'),
#         ('u','duplicate'),
#         ('g','good first issue'),
#         ('h','help wanted'),
#         ('i','invalid'),
#         ('q','question'),
#         ('w','wontfix'),
#         ('n','unassigned'),
#     )
#     PRIORITIES = (
#         ('H','High'),
#         ('M','Medium'),
#         ('L','Low'),
#     )
    
#     assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     description = models.TextField()
#     attachments = models.ManyToManyField(Attachment)
#     status = models.CharField(max_length=1, choices=STATUSES)
#     priority = models.CharField(max_length=1, choices=PRIORITIES)
#     labels = models.CharField(max_length=1, choices=LABELS)
#     deadline = models.DateField()

# class Comment(BaseModel):
#     message = models.TextField(max_length=150)
#     ticket = models.OneToOneField(Ticket)

