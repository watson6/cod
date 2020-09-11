from rest_framework.routers import DefaultRouter
from django.urls import path, include
from message.views import MessageViewSets

router = DefaultRouter()
router.register(r'message', MessageViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
