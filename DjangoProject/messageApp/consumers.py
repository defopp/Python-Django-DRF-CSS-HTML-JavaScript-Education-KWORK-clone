import json
import urllib.parse

from channels.generic.websocket import WebsocketConsumer
from django.db.models import Q

from .models import ChatRoom, Message
from usersApp.models import User

class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
       self.accept()
       
       print(self.scope['user'])
       self.send(text_data=json.dumps({
           'type':'connection_established',
           'message':'You are now connected!'
       }))
    

    def websocket_receive(self, message):
        query_dict = parse_message_text(message)
        print(query_dict)

        sender = User.objects.get(id=self.scope['user'].id) 
        interlocutor = User.objects.get(id=query_dict['intID'])
        chat_room_id = query_dict['chatRoomID']
        # decode text
        text = query_dict['text']
        text = urllib.parse.unquote(text, encoding='utf-8')
        text = urllib.parse.unquote(text, encoding='utf-8')

        # если чат рум не существует
        if chat_room_id == 'None':
            # проверка не появилась ли chatroom
            chat_room_qs = ChatRoom.objects.filter(Q(interlocutor = interlocutor.id) | Q(creater = interlocutor.id), Q(creater = sender.id) | Q(interlocutor = sender.id))
            if chat_room_qs.exists():
                # сохранить и отправить сообщение в существующуюю chatroom
                ...
            # создать chatrooom и отправить сообщение
            new_chat_room = ChatRoom(creater=sender, interlocutor=interlocutor)
            new_chat_room.save(force_insert=True)
            
            new_message = Message(owner=sender, chatroom=new_chat_room, text=text)
            new_message.save(force_insert=True)
            ...
        # если чат рум существует
        else:
            new_message = Message(owner=sender, chatroom=ChatRoom.objects.get(id=chat_room_id), text=text)
            new_message.save(force_insert=True)


        # отправить подтверждению отправителю 
            # ...
            
        # отправить сообщение получателю
            # ...





    def recive(self, text_data):
        ...        

    def disconnect(self, text_data):
        ...


def parse_message_text(message) -> dict:
    message_dict = {}
    text_list = message['text'].split('&')
    for query in text_list:
        query_list = query.split('=')
        message_dict[query_list[0]] = query_list[1]
    return message_dict