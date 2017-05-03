from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from django.contrib.auth import authenticate
from .models import *
from aloha.widgets import AlohaWidget
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password','type':'password'}))

    def clean(self,*args,**kwargs):
        username =self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("this user doest not exist")
        return super(LoginForm,self).clean(*args,**kwargs)


class comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

#class answerform(forms.Form):
#    ans = forms.CharField(max_length=20,widget=AlohaWidget)

class answerforms(forms.ModelForm):
    class Meta:
        model = Answer
        #widgets = SummernoteInplaceWidget
        fields = '__all__'

class Registrationform(UserCreationForm):
    first_name=forms.CharField(max_length=15)
    last_name=forms.CharField(max_length=15)
    email=forms.EmailField(error_messages={'required': 'already exist!'},widget=forms.TextInput(attrs={'type':"email",'class':"validate",'id':'email'}))
    #phone = forms.IntegerField()
    #phone = forms.IntegerField(widget=forms.TextInput(attrs={'type': "phone", 'class': "validate", 'id': 'phone','name':'phone'}))
    class Meta:
        model = User
        fields =("username","first_name","last_name","email")

    def clean(self,*args,**kwargs):
        ems=self.cleaned_data.get('email')
        u=self.cleaned_data.get('username')

        if User.objects.filter(username=u):
            raise forms.ValidationError("Username Already exist")
        if User.objects.filter(email=ems):
            raise forms.ValidationError("Email already exist")


        return self.cleaned_data




    def save(self,commit=True):
        user = super(Registrationform, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name=self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        #user.get_profile
        #user.profile.phone = self.cleaned_data["phone"]
        if commit:
            user.save()
        return user
