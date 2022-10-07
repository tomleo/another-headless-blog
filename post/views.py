from rest_framework import viewsets
from rest_framework import mixins

from post.models import Post
from post.serializers import PostSerializer

# from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class PostViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
