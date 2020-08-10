from rest_framework import routers
from .views import UserViewSet, BlogViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'blogs', BlogViewSet)