from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=UserRegister
        fields=('username','mobile','password','confirmPassword')

class notesForm(forms.ModelForm):
    class Meta:
        model=notesdata
        fields='__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model=UserRegister
        fields=['username','mobile']

class feedbackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'