from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User

from utilities.models import BaseModel


class ELibrary(BaseModel):
    owner = models.ForeignKey(to=User, on_delete=models.PROTECT)
    title = CharField(max_length=150)
    file = models.FileField(upload_to='media/e-library/')
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"ELibrary: {self.owner.email} - {self.title}"
    
    def get_absolute_url(self):
        pass


class Module(BaseModel):
    owner = models.ForeignKey(to=User, on_delete=models.PROTECT)
    title = CharField(max_length=150)
    file = models.FileField(upload_to='media/modules/')
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"Module: {self.owner.email} - {self.title}"

    def get_absolute_url(self):
        pass


class Documents(BaseModel):
    owner = models.ForeignKey(to=User, on_delete=models.PROTECT)
    title = CharField(max_length=150)
    file = models.FileField(upload_to='media/documents/')
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"Document: {self.owner.email} - {self.title}"

    def get_absolute_url(self):
        pass
