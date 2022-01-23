from django.urls import path, include
from . import views

from rest_framework import routers
from .views import BookViewSet

# we have a new variable router
router = routers.DefaultRouter()
# this BookViewset brings more than just a list
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
