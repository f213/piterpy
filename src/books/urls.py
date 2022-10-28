from django.urls import include, path
from rest_framework.routers import SimpleRouter

from books.api.views import BookViewSet

router = SimpleRouter()
router.register('', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
