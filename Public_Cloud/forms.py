from django import forms
class RegistrationForm(forms.Form):
	username = forms.CharField(label='Your name', max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.CharField(label='Your email', max_length=100)