from django.db import models

from djangotoolbox.fields import ListField

class Bill(models.Model):
    title = models.CharField()
    body = models.TextField()
    sections = ListField()
    comments = ListField()

