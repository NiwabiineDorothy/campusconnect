from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .validators import validate_must_email,validate

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(validators=[validate_must_email]) # default is when required is true -- adds this field also to the form
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2'] # field names of the user table


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(validators=[validate_must_email]) 
    class Meta:
        model = User
        fields = [ 'email', 'username']

class ProfileUpdateImgForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
class ProfileUpdateAboutForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['about']