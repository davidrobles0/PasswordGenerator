from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
	return render(request, 'generator/home.html', {'pass':'c0ntrasenia'})

def eggs(request):
	return HttpResponse("<h1>Los huevos son la leche</h1>")

def password(request):
	# Codigo en python para generar la contrasena aleatoria
	# de default todo entra como string
	length = int( request.GET.get('length', 12) ) # 12 seria el default

	contra = ''

	minus = 'abcdefghijklmnopqrstuvwxyz'
	mayus = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	numbers = '0123456789'
	especiales = '!·%&/*[]+´Ç_-<>)(#~'

	if request.GET.get('uppercase'):
		minus += mayus

	if request.GET.get('special'):
		minus += especiales

	if request.GET.get('numbers'):
		minus += numbers

	for i in range(int(length)):
		contra+=random.choice(minus)

	return render(request, 'generator/password.html', {'password': contra})

def about(request):
	return render(request, 'generator/about.html')