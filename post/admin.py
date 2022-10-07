from django.contrib import admin
from permissions.models import PermissionType
from post.models import Post, PostPermissionByEmail, PostPermissionByEmailPattern

class PostPermissionByEmailInline(admin.TabularInline):
    extra = 1
    model = PostPermissionByEmail
    show_change_link = True

class PostPermissionByEmailPatternInline(admin.TabularInline):
    extra = 1
    model = PostPermissionByEmailPattern

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    extra = 1
    inlines = [
        PostPermissionByEmailInline,
        PostPermissionByEmailPatternInline,
    ]
