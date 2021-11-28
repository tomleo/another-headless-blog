import re

from rest_framework.permissions import BasePermission

from post.models import Post


class CanReadPostGivenEmail(BasePermission):
    """
    If a requesting user's email matches the pattern return True
    """

    def has_permission(self, request, view):
        return False

    def has_object_permission(self, request, view, post: Post):
        for permission_pattern in post.post_permission_by_email_pattern.objects.all():
            return permission_pattern.permission_type.can_read and re.match(
                permission_pattern.pattern, request.email
            )
