from django import forms


class registration_form(forms.Form):
	email 		= forms.EmailField(label = 'Email', max_length = 254, 
						widget=forms.TextInput(attrs={'class' : 'mail_field'}))
	
	username 	= forms.CharField(label = 'Username', max_length = 254, 
						widget = forms.TextInput(attrs = {'class': 'username'}))

	password	= forms.CharField(label = 'Password', max_length = 254, widget = forms.PasswordInput())

class login_form(forms.Form):

	username	= 	username 	= forms.CharField(label = 'Username', max_length = 254, 
						widget = forms.TextInput(attrs = {'class': 'username'}))

	password	= forms.CharField(label = 'Password', max_length = 254, widget = forms.PasswordInput())

class add_form(forms.Form):

	when 		= forms.CharField(max_length = 200)
	courses		= forms.CharField(label = 'Courses', max_length = 500, widget = forms.TextInput(attrs = {'class': 'courses'}))
	pay			= forms.NullBooleanField()
	where		= forms.CharField(label = 'Place', max_length = 400, widget = forms.TextInput(attrs = {'class': 'where'}))

	