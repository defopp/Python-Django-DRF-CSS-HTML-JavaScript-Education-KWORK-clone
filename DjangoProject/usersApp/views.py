from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from tools import if_login


from .forms import SignUpForm, LogInForm, ChangePasswordForm, MainSettingsForm
from .models import User
from productsApp.models import Product


class signupView(View):
    template_name = 'usersApp/template/signup.html'

    def get(self, request):
        return render(request, self.template_name, {'form': SignUpForm()})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main')        
        return render(request, self.template_name, {'form': form})

            
class loginView(View):
    template_name = 'usersApp/template/login.html'
    
    def get(self, request):
        return render(request, self.template_name, {'form': LogInForm()})
    
    def post(self, request):
        form = LogInForm(request=request, data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
        return render(request, self.template_name, {'form': form})
 
 
class logoutView(View):
    def get(self, request):
        logout(request)
        return redirect('main')


class profileView(View):
    template_name = 'usersApp/template/profile.html'
    
    def get(self, request, user_id):
        try:
            user_pr = User.objects.all().filter(id = user_id).get()
        except Exception as ex:
            return HttpResponse(f'Пользователя с id {user_id} не существует')
            
        owner_projects = Product.objects.all().filter(owner_id=user_pr.id, sell_type=True)
        owner_orders = Product.objects.all().filter(owner_id=user_pr.id, sell_type=False)
        userprofile = {
            'user_pr':user_pr,
            'owner_projects':owner_projects,
            'owner_orders':owner_orders,
        }    
        return render(request, self.template_name, userprofile)


class myProfileView(View):
    template_name = 'usersApp/template/my_profile.html'
    
    @if_login
    def get(self, request):
            owner_projects = Product.objects.all().filter(owner_id=request.user.id, sell_type=True)
            owner_orders = Product.objects.all().filter(owner_id=request.user.id, sell_type=False)
            return render(request, self.template_name, {'owner_projects':owner_projects,
                                                        'owner_orders':owner_orders})

class editProfileView(View):
    template_name = 'usersApp/template/user_settings.html'

    @if_login
    def get(self, request):

        user = User.objects.get(username=request.user.username)
        # Добавить формы для общих настроек и смены пароля

        context = {
            'MainSettingsForm':MainSettingsForm(initial={
                "first_name":user.first_name,
                "last_name":user.last_name,
                "description":user.description
                }),
            'ChangePasswordForm':ChangePasswordForm(user),
        }        
        return render(request, self.template_name, context)
    
    @if_login
    def post(self, request): 
        if 'old_password' in request.POST :
            # change password form
            form = ChangePasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                username = request.user.username
                password = request.POST['old_password']
                new_password = request.POST['new_password1']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    form.save(commit=True)
                    user = authenticate(request, username=username, password=new_password)
                    login(request, user)
                    
                    context = {
                        'MainSettingsForm':MainSettingsForm(),
                        'ChangePasswordForm':form,
                        "change_pass_succes":"Пароль успешно изменен!"
                    }     
                    return render(request, self.template_name, context)   
                else:
                    return HttpResponse('Ошибка Авторизации')
                
            context = {
                'MainSettingsForm':MainSettingsForm(),
                'ChangePasswordForm':form
            }        
            return render(request, self.template_name, context)    
         
        elif 'first_name' in request.POST:
            # mainsettings form
            user = User.objects.get(username=request.user.username)
            if user is not None:
                form = MainSettingsForm(instance=user, data=request.POST, files=request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('user_settings') 
                return HttpResponse(f"form = невалид")
            return HttpResponse(f"user is none")
        
        else:
            return HttpResponse(f"Запрос не подходит ни под одну форму")
            
         
        


