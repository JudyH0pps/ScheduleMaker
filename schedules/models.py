from django.db import models
from django.conf import settings


class Schedule(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    # available_time = models.DateTimeField()

class Comment(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    date = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)