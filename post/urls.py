from rest_framework import routers

from post.views import PostViewSet

router = routers.SimpleRouter()
router.register(r"posts", PostViewSet)
urlpatterns = router.urls
