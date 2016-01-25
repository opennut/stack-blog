from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from django.core.context_processors import csrf
from django.contrib.auth.models import User, Group
from django.views.generic import FormView, TemplateView, RedirectView, ListView, CreateView
from django.views.generic import UpdateView, DetailView
from django.shortcuts import render, redirect, render_to_response
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse, reverse_lazy
# Authentication imports
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm	
from django.db.models import Q
from .forms import UploadFileForm
from models import UserProfile
from django.utils.translation import gettext as _
from allauth.account.utils import complete_signup
from allauth.account import app_settings
from allauth.account.forms import LoginForm


def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse("home"))
	else:
		if request.method == 'POST':
			form = RegisterForm(request.POST)
			
			x_user = User.objects.filter(email=request.POST["email"])
			if x_user.count() > 0:
				form.add_error('email', _('Este email ya existe'))
			else:
				if form.is_valid():
					current = form.save(commit=False)
					current.save()
					perfil = UserProfile()
					perfil.user = current
					perfil.save() 


					complete_signup(request, current,app_settings.EMAIL_VERIFICATION, "/")
					return HttpResponseRedirect(reverse("registered"))


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
'''
class LoginView(FormView):
    form_class = LoginForm
    template_name = "login.html"
    success_url =  reverse_lazy("login")

'''
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

class profile(DetailView):
	model = User
	slug_url_kwarg = "id"
	slug_field = "pk"
	fields = ("id", "username", "email")
	template_name = "profile.html"
	context_object_name = "x"

class user_upprofile(UpdateView):
    model = User
    fields = ['username','first_name','last_name']
    template_name = 'editprofile.html'
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user

def upload_file(request,id):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
			current = form.save(commit=False)
			current.user = request.user
			current.user.profile.delete()
			current.save()
			return HttpResponseRedirect('/')

    else:
        form = UploadFileForm()
    return render(request, 'editprofile.html', {'form': form})


def staff(request, id):
	user = request.user
	x = User.objects.get(id = id)
	group = Group.objects.get(name="moderadores")
	if user.is_superuser and user != x and not x.is_superuser:
		x.is_active = True
		x.groups.add(group)
		x.is_staff = True
		x.save()
	return HttpResponseRedirect(reverse("profile", args={ x.id }))

def active(request, id):
	user = request.user
	x = User.objects.get(id = id)
	if user.is_superuser and user != x and not x.is_superuser:
		x.is_active = True
		x.is_staff = False
		x.save()
	return HttpResponseRedirect(reverse("profile", args={ x.id }))

def inactive(request, id):
	user = request.user
	x = User.objects.get(id = id)
	if user.is_superuser and user != x and not x.is_superuser:
		x.is_active = False
		x.is_staff = False
		x.save()
	return HttpResponseRedirect(reverse("profile", args={ x.id }))

	
def registered(request):
	return render(request, 'registered.html')

def redirect(request):
	return HttpResponseRedirect(reverse("home"))
