from django.db.models import Q

from rest_framework.views import APIView   
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .models import ChatRoom
from .serializers import ChatRoomSerializer
        
class ChatRoomAPI(APIView):
    
    def get(self, request):
        user_id = request.user.id
        # ТЕСТИМ И ДЕБАЖИМ модель
        chat_rooms = ChatRoom.objects.all().filter(Q(interlocutor = user_id) | Q(creater = user_id)).select_related('creater', 'interlocutor')
        # print(chat_rooms.query)
        serializer = ChatRoomSerializer(chat_rooms, many=True)
        return Response({"requester_id":user_id,
                         "data":serializer.data})

    def post(self, request):
        ...

    def put(self, request):
        ...
    
    def delete(self, request):
        ...