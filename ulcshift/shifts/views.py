from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.edit import View
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import registration_form, login_form, add_form
from shifts.models import *
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

			tutor = Tutor(username = username, email = email)
			tutor.save()

			return HttpResponse("Created")


class login_user(View):
	
	form = login_form
	template_name = 'login.html'

	def get(self, request, *args, **kwargs):
		form = self.form
		return render(request, self.template_name, {'form':form})

	def post(self, request, *args, **kwargs):
		form = self.form(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(username = username, password = password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse("Okay")
				else:
					return HttpResponse("Sorry your account is not active yet")
			else:
				return HttpResponseRedirect("Invalid password or username")

		return HttpResponse("okat")


class SubMain(View):

	form = add_form
	template_name = 'add.html'

	def get(self, request, *args, **kwargs):
		form = self.form
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):

		form = self.form(request.POST)

		if form.is_valid():
			when = form.cleaned_data['when']
			where = form.cleaned_data['where']
			courses = form.cleaned_data['courses']
			pay = form.cleaned_data['pay']

			sub = Subs(where = where, pay = pay, courses = courses, by = Tutor.objects.get(username = request.user.username), time = when)
			sub.save()

			return HttpResponse("Okay")


class Dashboard(View):

	template_name = 'dash.html'
	def get(self, request, *args, **kwargs):
		o = Subs.objects.all()
		return render(request, self.template_name, {'o':o})


class Take(View):
	template_name = "take.html"
	def get(self, request, pk, *args, **kwargs):
		




