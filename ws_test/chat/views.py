from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from chat.models import Message
from chat.serializers import MessageSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
