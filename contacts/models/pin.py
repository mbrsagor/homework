from datetime import datetime, timedelta

from contacts.models.base import BaseEntity
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string


class PinRecoverySessionManager(models.Manager):
    def get_live_session(self, token):
        session = get_object_or_404(self, token=token)
        if session.is_token_alive:
            return session
        else:
            raise Http404("Session expired")



class PinRecoverySession(models.Model):
    question = JSONField(blank=True, null=True)
    phone_number = models.CharField(max_length=125)
    token = models.CharField(max_length=250, blank=True, null=True, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)
    expire_time = models.DateTimeField()
    is_alive = models.BooleanField(default=True)

    objects = PinRecoverySessionManager()

    @property
    def is_token_alive(self):
        is_alive = datetime.now() <= self.expire_time and self.is_alive
        return is_alive

    def kill(self):
        self.is_alive = False
        self.save()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.expire_time = datetime.now() + timedelta(hours=1)  # set 1 hour expire time
        self.token = get_random_string(32)  # generate 32 length random string in every step
        super(PinRecoverySession, self).save(*args, **kwargs)

    def __str__(self):
        return self.phone_number
