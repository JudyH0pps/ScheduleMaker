from django import forms
from .models import Schedule, Comment


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        exclude = ['user']

class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['date']

class GuestCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['schedule', 'user']