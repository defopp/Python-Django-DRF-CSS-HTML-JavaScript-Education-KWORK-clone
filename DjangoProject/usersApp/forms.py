from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm


from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Логин'}), 
        }
        

class LogInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password','error_messages')

        
        
class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password',"new_password1","new_password2")
        
        
class MainSettingsForm(forms.Form):
    avatar = forms.ImageField()
    first_name = forms.CharField(label='Имя', max_length=150, widget=forms.TextInput(attrs={"placeholder":'Имя'}))
    last_name = forms.CharField(label='Фамилия', max_length=150, widget=forms.TextInput(attrs={"placeholder":'Фамилия'}))
    description = forms.CharField(help_text='Хелп текст',label='Описание', max_length=400, widget=forms.Textarea(attrs={"placeholder":'Описание'}))
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'description', 'avatar')