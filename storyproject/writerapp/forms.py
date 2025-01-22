from django import forms
from django.contrib.auth.models import User
from writerapp.models import StoryModel

class UserSignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}),
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}),
        }

class UserSignInForm(forms.ModelForm):
    USER_TYPE_CHOICES = [

        ('writer', 'writer'),
        ('viewer', 'viewer'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, label="User Type")

    class Meta:
        model = User
        fields = ['username', 'password']  # Use fields from the User model
        widgets = {
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Usename"}),
            'password': forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}),  # Password as hidden input
        }
        

class StoryForm(forms.ModelForm):
    class Meta:
        model = StoryModel
        fields = ['title', 'description', 'image']

class StoryEditForm(forms.ModelForm):
    class Meta:
        model=StoryModel
        fields=["title","description","image"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"title"}),
            "description":forms.TextInput(attrs={"class":"form-control","placeholder":"description"}),
        }