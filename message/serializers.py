from rest_framework.serializers import ModelSerializer
from message.models import Message


class MessageListSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'project', 'type', 'host', 'title', 'level', 'status', 'time']


class MessageRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

