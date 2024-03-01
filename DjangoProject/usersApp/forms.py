from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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
        widgets = {
            'username': {'placeholder': 'Логинфыыфы'},
        }
        
        