from django.db import models

class Bill(models.Model):
    title = models.CharField(max_length=32)
    body = models.TextField()
    class Meta:
        db_table = 'bill'
        app_label = 'legislation_editor' 
