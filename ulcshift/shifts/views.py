from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.edit import View
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import registration_form
# Create your views here.

# Create your views here.
class register(View):

	form = registration_form
	template_name = "register.html"

	def get(self, request):
		form = self.form
		return render(request, self.template_name, {'form': self.form})

	def post(self, request):
			form = self.form

			username = request.POST.get('username', False)
			password = request.POST.get('password', False)
			email	 = request.POST.get('email', False)
			
			user = User.objects.create_user(username, email, password)
			user.save()

			return HttpResponse("Created")