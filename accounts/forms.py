from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class RegisterForm(UserCreationForm):
    # declare the fields you will show
    username = forms.CharField(label=_("Nombre de Usuario"), required=True)
    # first password field
    password1 = forms.CharField(label=_("Tu Contrasena"),widget=forms.PasswordInput, required=True)
    # confirm password field
    password2 = forms.CharField(label=_("Repite tu Contrasena"),widget=forms.PasswordInput, required=True)
    email = forms.EmailField(label = _("Correo Electronico"), required=True)
    first_name = forms.CharField(label = _("Nombre"), required=True)
    last_name = forms.CharField(label = _("Apellido"), required=True)
 
    # this sets the order of the fields
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2", )

	# this redefines the save function to include the fields you added
	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		user.first_name = self.cleaned_data["first_name"]
		user.last_name = self.cleaned_data["last_name"]
		if commit:
			user.save()


class UploadFileForm(forms.ModelForm):
    class Meta: 
        model = UserProfile
        fields = ('image',)