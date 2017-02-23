from __future__ import unicode_literals

from django.db import models


class Videos(models.Model):
    actor = models.CharField(max_length=200)
    video_title = models.CharField(max_length=200)
    dateOfRelease = models.DateField(auto_now=False)

    def __str__(self):
        return self.actor + " - " + self.video_title 
