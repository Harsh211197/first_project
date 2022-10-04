from django import forms
from .models import Board,Topic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Registrationform(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']

class BoardRegistrationform(forms.ModelForm):
    class Meta:
        model=Board
        fields=['name','description','board_starter']

class TopicRegistrationform(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['subject','board','starter']
    
# class PostRegistrationform(forms.ModelForm):
#     class Meta:
#         model=Post
#         fields=['message','topic']

# class TopicRegistrationform(forms.ModelForm):
#     class Meta:
#         model=Board
