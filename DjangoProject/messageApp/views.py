from django.shortcuts import render, HttpResponse
from django.views import View

from messageApp.models import ChatRoom

# Create your views here.
class ChatView(View):
    template_name = 'messageApp\\template\\messenger.html'
    
    def get(self, request):
        # WAY ONE open to chat/ if request.data == i want ot talk with him... => context: instant create form
        if len(request.GET) > 0:
            requester_id = request.user.id
            if 'intID' in request.GET:
                interlocutor_id = request.GET['intID']
                return render(request, self.template_name, {'type_of_chat' : 'PeerToPeer'})

        # WAY TWO mainopen/ else
        else:
            return render(request, self.template_name)
    
    def post(self, request):
        return HttpResponse('[http post request] request - done')






    

