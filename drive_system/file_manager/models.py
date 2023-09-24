from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Folder(models.Model):
    name = models.CharField(max_length=255, default = "untitled Folder")
    parent_folder = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=255, default = "untitled Folder")
    parent_folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/',default=False)
    
    def __str__(self):
        return self.name

class User(models.Model):
    pass