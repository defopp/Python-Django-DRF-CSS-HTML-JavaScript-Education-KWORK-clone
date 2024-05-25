import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
       self.accept()
       
       print(self.scope['user'])
       self.send(text_data=json.dumps({
           'type':'connection_established',
           'message':'You are now connected!'
       }))
    

    def websocket_receive(self, message):
        print(message)
        

    def recive(self, text_data):
        ...        

    def disconnect(self, text_data):
        ...