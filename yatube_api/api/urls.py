from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, GroupViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
