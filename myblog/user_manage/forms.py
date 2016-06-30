from django import forms

class EmailForm(forms.Form):
    email = forms.CharField(label='E-mail')
    content = forms.CharField(label='Content')

class LoginForm(forms.Form):
    name = forms.CharField(label='User Name')
    pw = forms.CharField(label='Password')