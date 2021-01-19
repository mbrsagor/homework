from django.db import models
from contacts.models.base import BaseEntity


class Type(BaseEntity):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=80)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
