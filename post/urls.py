from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter()

router.register('list', views.PostViewset)
router.register('like', views.PostLikeViewset)
router.register('unlike', views.PostUnlikeViewset)
router.register('comment', views.CommentViewset)
urlpatterns = [
    path('', include(router.urls)),
]