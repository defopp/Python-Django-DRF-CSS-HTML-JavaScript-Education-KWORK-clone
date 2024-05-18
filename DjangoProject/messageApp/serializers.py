from rest_framework import serializers
from rest_framework import serializers

from .models import ChatRoom, Message
from usersApp.serializers import UserSerializer




class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'






class ChatRoomsSerializer(serializers.ModelSerializer):
    creater = UserSerializer()
    interlocutor = UserSerializer()
    last_message = MessageSerializer()

    class Meta:
        model = ChatRoom
        # fields = '__all__'
        fields = ['id', 'creater', 'interlocutor', 'product', 'start_date', 'last_message']


class ChatRoomSerializer(serializers.ModelSerializer):
    creater = UserSerializer()
    interlocutor = UserSerializer()
    all_messages = MessageSerializer(many=True)

    class Meta:
        model = ChatRoom
        # fields = '__all__'
        fields = ['id', 'creater', 'interlocutor', 'product', 'start_date', 'all_messages']


