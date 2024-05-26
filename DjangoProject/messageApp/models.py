from django.db import models

from usersApp.models import User
from productsApp.models import Product


# Create your models here.
class ChatRoom(models.Model):
    creater = models.ForeignKey(User, related_name='creater_id', on_delete=models.PROTECT)
    interlocutor = models.ForeignKey(User, related_name='interlocutor_id', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.PROTECT, null=True, blank=True)
    start_date = models.DateTimeField('Дата создания', auto_now=True)

    def __str__(self) -> str:
        return f'{self.id} ({self.creater}) to ({self.interlocutor})'
        ...

    def last_message(self):
        last_message = Message.objects.filter(chatroom = self.id).order_by("-id")
        if last_message.exists():
            return last_message[0]
        return None
    
    def all_messages(self):
        all_messages = Message.objects.filter(chatroom = self.id).order_by("id")
        return all_messages



class Message(models.Model):
    owner = models.ForeignKey(User, related_name='owner_id', on_delete=models.PROTECT)
    chatroom = models.ForeignKey(ChatRoom, related_name='chatroom_id', on_delete=models.PROTECT)
    # type 0 basic message / 1 system message
    type = models.IntegerField(default=0)
    date = models.DateTimeField('Дата сообщения', auto_now=True)
    text = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return f"chatroom_id - {self.chatroom}; message_id - {self.id}"
        ...
