from api.views import PostViewSet, UserViewSet, CommentViewSet, AlbumViewSet, PhotoViewSet, TodoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'todos', TodoViewSet)