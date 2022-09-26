from rest_framework import routers
from django.urls import include, path
from api.views import (UserViewSet, GenreViewSet, TitleViewSet,
                       CategoryViewSet, ReviewViewSet, CommentViewSet,
                       signup, token)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'titles', TitleViewSet, basename='titles')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet,
                basename='reviews')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/signup/', signup, name='signup'),
    path('auth/token/', token, name='token'),
]
