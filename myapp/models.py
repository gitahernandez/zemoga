from django.db import models

class File(models.Model):
    docfile = models.FileField(upload_to='')
    kind = models.CharField(max_length=20, default='')
    file_name = models.CharField(max_length=100, default='')