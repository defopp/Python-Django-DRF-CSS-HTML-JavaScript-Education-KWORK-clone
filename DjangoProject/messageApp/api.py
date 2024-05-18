from django.db.models import Q, Max

from rest_framework.views import APIView   
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .models import ChatRoom, Message, User
from .serializers import ChatRoomsSerializer, ChatRoomSerializer, UserSerializer
        
class ChatRoomsAPI(APIView):
    
    def get(self, request):
        user_id = request.user.id
        #
        # TODO: Оптимизировать запрос в ChatRoom к last_message
        chat_rooms = ChatRoom.objects.all().filter(Q(interlocutor = user_id) | Q(creater = user_id)).select_related('creater', 'interlocutor')
        # print(chat_rooms.query)
        serializer = ChatRoomsSerializer(chat_rooms, many=True)
        return Response({"requester_id":user_id,
                         "data":serializer.data})

    def post(self, request):
        ...

    def put(self, request):
        ...
    
    def delete(self, request):
        ...

# Запрос для создания формы чата(собеседнике и все сообщения)
class ChatRoomAPI(APIView):

    def get(self, request):
        requester_id = request.user.id

        if 'intID' in request.GET:
            chat_room = ChatRoom.objects.filter(Q(interlocutor = request.GET['intID']) | Q(creater = request.GET['intID']), Q(creater = requester_id) | Q(interlocutor = requester_id))
            if chat_room.exists():
                serializer = ChatRoomSerializer(chat_room.get())
                return Response({"requester_id":requester_id,
                                "data":serializer.data})
            else:

                creater_ser = UserSerializer(request.user)
                int_ser = UserSerializer(User.objects.get(id = request.GET['intID']))
                response = {
                    'requester_id': requester_id,
                    'data': {
                        'creater':creater_ser.data,
                        'id':'None',
                        'interlocutor':int_ser.data
                    }
                }
                return Response(response)



            if 'prodID' in request.GET:
                ...
            ...
        else:
            return Response({'data':'none',
                            'description':'request without params'})
        


        if 'chatroomID' in request.GET:
            ...