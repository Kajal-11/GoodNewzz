from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User


class UserRegisterForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model 	= User
		fields 	= ['name', 'email', 'contact', 'password1', 'password2']
	
	@transaction.atomic
	def clean(self):
		email = self.cleaned_data.get('email')

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("Account with this email already exists")
		return self.cleaned_data
