from django.shortcuts import render, HttpResponse


def home(request):
	return HttpResponse("inio")

def servicio(request):
	return HttpResponse("servicio")

def tienda(request):
	return HttpResponse("tienda")

def blog(request):
	return HttpResponse("blog")

def contacto(request):
	return HttpResponse("contacto")