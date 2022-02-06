from django.db import models
from django.forms import ModelForm
from .models import Client

class ClientForm(ModelForm):
	class Meta:
		model = Client
		#fields = ['nom', 'email', 'date_naiss', 'sexe', 'telephone', 'date_sous']
		exclude = ['created','updated']
