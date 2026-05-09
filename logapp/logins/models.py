from django.db import models
from django.contrib.auth.models import User



class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField('log timestamp')
    login = models.CharField(max_length=10)
    note = models.ForeignKey('Note', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username+', '+self.login+', '+str(self.time.ctime()) +\
        (', note: ' + self.note.note_content if self.note else '')


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note_content = models.CharField(max_length=150)

    def __str__(self):
        return self.user.username+': '+self.note_content
