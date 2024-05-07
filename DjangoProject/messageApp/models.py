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


class Message(models.Model):
    owner = models.ForeignKey(User, related_name='owner_id', on_delete=models.PROTECT)
    chatroom = models.ForeignKey(ChatRoom, related_name='chatroom_id', on_delete=models.PROTECT)
    type = models.IntegerField
    date = models.DateTimeField('Дата сообщения', auto_now=True)

    def __str__(self) -> str:
        return f"chatroom_id - {self.chatroom}; message_id - {self.id}"
    ...