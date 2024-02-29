from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm, LogInForm


class signupView(View):
    template_name = 'usersApp\\template\\signup.html'

    def get(self, request):
        context = {
            'form': SignUpForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

            
class loginView(View):
    template_name = 'usersApp\\template\\login.html'
    
    def get(self, request):
        context = {
            'form': LogInForm()
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = LogInForm(request=request, data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
        
            
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class logoutView(View):
    def get(self, request):
        logout(request)
        return redirect('main')














# def signup(request):
#     if request.method == "POST":
#         return HttpResponse('registraciya')
    
    
#     return render(request, 'usersApp\\template\\signup.html', {'form' : SignUpForm})
    
    
    
    
    
    # ### Логика SignUp ###
    # login = request.POST['field_login']
    # password = request.POST['field_password']
    # newUser = User(username=login,password=password)


# def login(request):
#     return render(request, 'usersApp\\template\\login.html', {'form' : LogInForm})

    
    
    
    
    
    
    

    ### Логика LogIn ###
    # login = request.POST['login']
    # password = request.POST['password']
    # if request == "POST":
    #     return HttpResponse('Залогинился??')

    
