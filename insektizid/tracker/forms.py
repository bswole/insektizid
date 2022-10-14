from django import forms

class TimeStampedModelCreationForm(forms.BaseModelForm):
    pass
class TimeStampedModelChangeForm(forms.BaseModelForm):
    pass

class ProjectCreationForm(TimeStampedModelCreationForm):
    pass
class ProjectChangeForm(TimeStampedModelChangeForm):
    pass

class TicketCreationForm(TimeStampedModelCreationForm):
    pass
class TicketChangeForm(TimeStampedModelChangeForm):
    pass

class CommentCreationForm(TimeStampedModelCreationForm):
    pass
class CommentChangeForm(TimeStampedModelChangeForm):
    pass

class AttachementCreationForm(TimeStampedModelCreationForm):
    pass
class AttachementChangeForm(TimeStampedModelChangeForm):
    pass
