from rest_framework import serializers
from post.models import Post, PostPermissionByEmail, PostPermissionByEmailPattern

class PostPermissionByEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPermissionByEmail
        fields = [
            "id",
            "created",
            "modified",
            "email",
            "permission_type",
        ]

class PostPermissionByEmailPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPermissionByEmailPattern
        fields = [
            "id",
            "created",
            "modified",
            "name",
            "pattern",
            "description",
            "post",
            "permission_type",
        ]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "created",
            "modified",
            "body",
            "body_lang",
            "meta",
            "meta_lang",
            "publish_date",
            "last_edit_date",
            "authentication",
            "user",
        ]
