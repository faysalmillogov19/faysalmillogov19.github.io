from django.shortcuts import render, redirect
from .modelforms import ClientForm
from .models import Client 
import pandas as pd
from django.core.files.storage import default_storage
from django.db.models import Sum
import matplotlib.pyplot as plt

from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg

from io import BytesIO
import base64
import numpy as np

import os
import shutil

from datetime import date

# Create your views here.
def index(request):
	clients=Client.objects.all()
	
	return render(request, 'liste.html',{'clients':clients})

def form(request, id):

	data=''
	if int(id)>0:
		data=Client.objects.get(pk=id)

	return render(request,'ClientForm.html',{'data':data})

def Manageclient(request):

	if request.POST.get('id'):
		client=Client.objects.get(pk=request.POST.get('id'))
	else:
		client=Client()

	client.nom=request.POST.get('nom')
	client.date_naiss=request.POST.get('date_naiss')
	client.sexe=request.POST.get('sexe')
	client.email=request.POST.get('email')
	client.date_sous=request.POST.get('date_sous')
	client.telephone=request.POST.get('tel')
	client.save()

	return redirect('/clients/list')

def delete(request, id):
	Client.objects.filter(id=id).delete()
	return redirect('/clients/list')

def export(request):
	clients=Client.objects.all()
	data=[]
	for c in clients:
		k=[c.nom,c.date_naiss,c.sexe,c.email,c.telephone,c.date_sous]
		data.append(k)

	data=pd.DataFrame(data,columns =['nom','date_naiss','sexe','email','telephone','date_sous'])
	print(data)
	datatoexcel = pd.ExcelWriter('CarsData1.xlsx')
	data.to_excel(datatoexcel)
	datatoexcel.save()
	return redirect('/clients/list')


def importer(request):

	if request.POST:
		fichier = request.FILES['file']
		name = fichier.name
		file_name = default_storage.save('static/uploads/'+name, fichier)
		print(file_name)
		df = pd.read_excel(file_name)
		
		for index, d in df.iterrows():
			client=Client()
			client.nom=d.nom
			print(d.nom)
			client.date_naiss=d.date_naiss
			client.sexe=d.sexe
			client.email=d.email
			client.date_sous=d.date_sous
			client.telephone=d.telephone
			client.save()
		
		return redirect('/clients/list')

	else:
		return render(request,'import.html')

def stat_sex(request):
	clients=Client.objects.all()
	data=[]
	for c in clients:
		k=[c.nom,c.date_naiss,c.sexe,c.email,c.telephone,c.date_sous]
		data.append(k)
	df=pd.DataFrame(data, columns=['nom','date_naiss','sexe','email','telephone','date_sous'])
	df.groupby('sexe').count().plot(kind='bar')
	#fig, ax = plt.subplots()
	#ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
	file_name='test'
	plt.title('Representation en diagrame par sexe')
	plt.savefig(file_name)
	shutil.move("test.png", "static/uploads/stats/graphic.png")

	return render(request,'stats.html')


def stat_age(request):
	clients=Client.objects.all()
	data=[]
	for c in clients:
		k=[c.nom,int(date.today().year)-int(c.date_naiss.year),c.sexe,c.email,c.telephone,c.date_sous]
		data.append(k)
	df=pd.DataFrame(data, columns=['nom','age','sexe','email','telephone','date_sous'])
	df.groupby('age').count().plot(kind='bar')
	#fig, ax = plt.subplots()
	#ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
	file_name='test'
	plt.title('Representation en diagrame par sexe')
	plt.savefig(file_name)
	shutil.move("test.png", "static/uploads/stats/graphic.png")

	return render(request,'stats.html')