from django.contrib import admin
from permissions.models import PermissionType

# Register your models here.
@admin.register(PermissionType)
class PermissionTypeAdmin(admin.ModelAdmin):
    pass
