from rest_framework import serializers
from rest_framework import serializers

from .models import ChatRoom
from usersApp.serializers import UserSerializer




class ChatRoomSerializer(serializers.ModelSerializer):
    creater = UserSerializer()
    interlocutor = UserSerializer()

    class Meta:
        model = ChatRoom
        # fields = '__all__'
        fields = ['creater', 'interlocutor', 'product', 'start_date']


