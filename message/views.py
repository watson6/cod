from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from utils.drf.mixins import MultiSerializersMixin
from message.models import Message
from message.serializers import MessageListSerializer, MessageRetrieveSerializer


class MessageViewSets(MultiSerializersMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Message.objects.filter(is_enabled=True, is_deleted=False)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    serializer_class_mapping = {
        'list': MessageListSerializer,
        'retrieve': MessageRetrieveSerializer
    }
    search_fields = ['project', 'type', 'host', 'title', 'desc']
