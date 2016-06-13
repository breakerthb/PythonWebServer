from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(label='User Name')
    pw = forms.CharField(label='Password')