from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.views import View
from administration.models import User
from django.contrib.auth.forms import PasswordChangeForm

class UserLogoutView (View):
	def post (self, request, *args, **kwargs):
		logout(request)
		return redirect('index')

class UserChangePassword(View):
	template_name = 'users/change_password.html'
	def post (self, request, *args, **kwargs):
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			return redirect('index')
	def get (self, request, *args, **kwargs):
		form = PasswordChangeForm(request.user)
		return render(request, self.template_name, {'form': form})

class IndexView(View):
	template_name = 'users/index.html'
	def get (self, request, *args, **kwargs):
		return render(request, self.template_name, {})
