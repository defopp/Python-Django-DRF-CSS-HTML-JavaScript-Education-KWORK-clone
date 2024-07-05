from django.shortcuts import render, HttpResponse, redirect
from django.views import View

from tools import if_login

# Create your views here.
class ChatView(View):
    template_name = 'messageApp/template/messenger.html'

    @if_login
    def get(self, request):
        if request.user.is_authenticated:
            if len(request.GET) > 0:
                requester_id = request.user.id
                if 'intID' in request.GET:
                    interlocutor_id = request.GET['intID']
                    return render(request, self.template_name, {'type_of_chat' : 'PeerToPeer'})

            # WAY TWO mainopen/ else
            else:
                return render(request, self.template_name)
        else: return redirect('signup')







    

