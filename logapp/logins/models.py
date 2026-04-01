from django.db import models
from django.contrib.auth.models import User



class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField('log timestamp')
    note = models.ForeignObject(Note)


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note_content = models.CharField(max_length=150)