from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout


from .forms import SignUpForm, LogInForm
from .models import User
from productsApp.models import Product


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


class profileView(View):
    template_name = 'usersApp\\template\\profile.html'
    
    def get(self, request, pk):
        
        try:
            user = User.objects.get(id = pk)
    
            """проверяю есть ли пользователь с таким PrimaryKey в Базе данных
            Если он есть, то распаковываю QuerySet в dict userprofile,
            и отправляю на шаблон с контекстом userprofile"""
            owner_projects = Product.objects.all().filter(owner_id=user.id)
            userprofile = {
                'user':user,
                'owner_projects':owner_projects
            }    
            return render(request, self.template_name, userprofile)
        except Exception:
            return HttpResponse('404')









