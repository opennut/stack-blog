from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.views.generic import FormView, TemplateView, RedirectView, ListView
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
# Authentication imports
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm	
from django.db.models import Q
from .models import Perfil
from django.utils.translation import gettext as _

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		print request.POST
		
		x_user = User.objects.filter(email=request.POST["email"])
		if x_user.count() > 0:
			form.add_error('email', _('Este email ya existe'))
		else:
			if form.is_valid():
				current = form.save(commit=False)
				current.save()
				perfil = Perfil()
				perfil.user = current
				perfil.save()

				user = authenticate(username=request.POST["username"], password=request.POST["password1"])
				login(request, user)

				return HttpResponseRedirect(reverse('home'))
	else:
		form = RegisterForm()
	return render(
		request, 
		'register.html',
			{
				"form": form
			}
		)

def logout_on(request):
	logout(request)
	return HttpResponseRedirect(reverse("home"))

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url =  reverse_lazy("login")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)
            return HttpResponse(_("Tu usuario y tu contrasena no concuerdan"))

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class UserListView(ListView):
	model = User
	template_name = "users.html"
	context_object_name = "users_list"
	ordering = "last_login"

	def get_queryset(self):
		qs = super(UserListView, self).get_queryset()
		filter_name = self.request.GET.get('username', None)
		if filter_name != None:
			qs = qs.filter(Q(username__contains=filter_name) | Q(first_name__contains=filter_name) | Q(last_name__contains=filter_name))
		return qs

