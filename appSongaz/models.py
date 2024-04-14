import uuid
import os
from django.db import models
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


def generate_unique_id():
    return str(uuid.uuid4())[:4]


class File(models.Model):
    title = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="files", on_delete=models.CASCADE)
    arrived = models.BooleanField(default=True)
    unique_id = models.CharField(max_length=4, unique=True, default=generate_unique_id)

    def __str__(self):
        return os.path.basename(self.file.name)

    def filename(self):
        return os.path.basename(self.file.name)[:10]

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = os.path.basename(self.file.name)
        super().save(*args, **kwargs)
