from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)

router_v1 = DefaultRouter()

router_v1.register(
    prefix='titles',
    viewset=TitleViewSet,
    basename='titles',
)
router_v1.register(
    prefix='categories',
    viewset=CategoryViewSet,
    basename='categories',
)
router_v1.register(
    prefix='genres',
    viewset=GenreViewSet,
    basename='genres',
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='review'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
