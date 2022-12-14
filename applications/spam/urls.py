from django.urls import path
from rest_framework.routers import DefaultRouter

from applications.spam.views import SpamApiView

router = DefaultRouter()
router.register('', SpamApiView)

urlpatterns = router.urls
