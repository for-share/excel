from django.contrib.auth.models import User
from django.db import models


class Files(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    file = models.FileField(upload_to='uploads/')

