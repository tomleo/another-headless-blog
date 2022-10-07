"""
This is the app for posts

A better docstring to come soon
"""

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import (
    AutoSlugField,
    CreationDateTimeField,
    ModificationDateTimeField,
)

from permissions.models import PermissionType

User = get_user_model()


class Post(models.Model):
    """
    Each post has a record
    """

    class BodyLanguages(models.TextChoices):
        """
        These are the supported languages for the server
        """

        MARKDOWN = "markdown", _("Markdown")
        # PLAIN_TEST = 'plain_test', _('Plain Text')
        # HTML = 'html', _('HTML')

    class MetaLanguages(models.TextChoices):
        """
        These are the supported languages for post meta data
        """

        JSON = "json", _("JSON")

    title = models.CharField(_("title"), max_length=512)
    slug = AutoSlugField(_("slug"), max_length=512, populate_from="title")
    created = CreationDateTimeField(_("created"))
    modified = ModificationDateTimeField(_("modified"))
    body = models.TextField()
    body_lang = models.CharField(
        max_length=32, choices=BodyLanguages.choices, default=BodyLanguages.MARKDOWN
    )
    meta = models.TextField()
    meta_lang = models.CharField(
        max_length=32, choices=MetaLanguages.choices, default=MetaLanguages.JSON
    )
    publish_date = models.DateField(blank=True, null=True)
    last_edit_date = models.DateField(blank=True, null=True)
    authentication = models.BooleanField(default=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def get_post_permissions_by_email(self):
        return self.postpermissionbyemail_set.all()
    
    def get_post_permissions_by_pattern(self):
        return self.postpermissionbyemailpattern_set.all()


class PostPermissionByEmail(models.Model):
    """
    Permission records for a post

    Access to a post can be determined by checking related permissions
    """

    created = CreationDateTimeField(_("created"))
    modified = ModificationDateTimeField(_("modified"))
    email = models.EmailField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    permission_type = models.ForeignKey(PermissionType, on_delete=models.PROTECT)


class PostPermissionByEmailPattern(models.Model):
    """
    Permission by regex instead of a permission by email

    For example you could do r"(?P<any_employee>.+)@(?P<domain>your-company\.com)"
    """

    created = CreationDateTimeField(_("created"))
    modified = ModificationDateTimeField(_("modified"))
    name = models.CharField(max_length=256)
    pattern = models.TextField()
    description = models.TextField(blank=True, default="")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    permission_type = models.ForeignKey(PermissionType, on_delete=models.PROTECT)
