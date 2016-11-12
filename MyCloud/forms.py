#from wtforms import Form, BooleanField, StringField, PasswordField, validators
from django import forms
class RegistrationForm(forms.Form):
    # username = StringField('Username', [validators.Length(min=4, max=25)])
    # email = StringField('Email Address', [validators.Length(min=6, max=35)])
    # password = PasswordField('New Password', [
        # validators.DataRequired(),
        # validators.EqualTo('confirm', message='Passwords must match')
    # ])
    # confirm = PasswordField('Repeat Password')
    # accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
	username = forms.CharField(label='Your name', max_length=100)
	password = forms.CharField(label='Your password', max_length=100)
	email = forms.CharField(label='Your email', max_length=100)