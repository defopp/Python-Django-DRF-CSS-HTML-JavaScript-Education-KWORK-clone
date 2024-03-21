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
        
        
class MainSettingsForm(forms.ModelForm):
    avatar = forms.ImageField(required=False, label='Фотография', widget=forms.FileInput(attrs={'class':'imgfield'}))
    first_name = forms.CharField(required=False, help_text='До 150 знаков', label='Имя', min_length=1, max_length=150, widget=forms.TextInput(attrs={"placeholder":'Имя'}))
    last_name = forms.CharField(required=False, help_text='До 150 знаков', label='Фамилия', min_length=1, max_length=150, widget=forms.TextInput(attrs={"placeholder":'Фамилия'}))
    description = forms.CharField(required=False, help_text='До 1000 знаков',label='Описание', min_length=1, max_length=1000, widget=forms.Textarea(attrs={"placeholder":'Описание'}))
    
    class Meta:
        model = User
        fields = ('avatar', 'first_name', 'last_name', 'description')
        