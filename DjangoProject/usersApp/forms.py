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
        