"""
This is the app for permissions

A better docstring to come soon
"""

from django.db import models


# Create your models here.
class PermissionType(models.Model):
    """
    Keep track of permission types
    """

    name = models.CharField(max_length=256)
    can_read = models.BooleanField(default=False)
    can_write = models.BooleanField(default=False)

    def __str__(self):
        rw = []
        if self.can_read:
            rw.append("R")
        if self.can_write:
            rw.append("W")
        return "%s (%s)" % (self.name, ','.join(rw))
