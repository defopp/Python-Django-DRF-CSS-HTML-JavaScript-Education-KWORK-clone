from django.shortcuts import render
from django.views import View

from rest_framework import viewsets

# Create your views here.
class ChatView(View):
    template_name = 'messageApp\\template\\messenger.html'
    def get(self, request):
        return render(request, self.template_name)
    
    
# class MessageViewSet(viewsets.ModelViewSet):
#     ...    

