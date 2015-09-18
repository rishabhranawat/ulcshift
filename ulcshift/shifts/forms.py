from django import forms


class registration_form(forms.Form):
	email 		= forms.EmailField(label = 'Email', max_length = 254, 
						widget=forms.TextInput(attrs={'class' : 'mail_field'}))
	
	username 	= forms.CharField(label = 'Username', max_length = 254, 
						widget = forms.TextInput(attrs = {'class': 'username'}))

	password	= forms.CharField(label = 'Password', max_length = 254, widget = forms.PasswordInput())
