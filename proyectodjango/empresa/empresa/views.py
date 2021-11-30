from django.http import HttpResponse

def Saludos(request): #primera vista
	return HttpResponse("hola mundo, esta es mi primera pagina con django")