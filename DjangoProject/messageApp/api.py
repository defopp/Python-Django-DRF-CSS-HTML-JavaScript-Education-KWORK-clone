from rest_framework.views import APIView   
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .models import ChatRoom
from .serializers import ChatRoomSerializer
        
class ChatRoomAPI(APIView):
    
    def get(self, request):
        chat_rooms = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(chat_rooms, many=True)
        return Response(serializer.data)

    def put(self, request):
        ...
    
    def delete(self, request):
        ...