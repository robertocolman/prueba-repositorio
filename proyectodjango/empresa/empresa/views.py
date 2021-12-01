from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime

class persona(object):

	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido

def paginaPrincipal(request): #primera vista
	
	temas_del_curso = ["plantillas", "modelos", "formularios", "vistas", "despliegue"]

	p1 = persona("Robert", "Colman")

	ahora = datetime.datetime.now()

	#doc_externo = get_template('miplantilla.html')

	#doc_externo=open("C:/Users/rober/Desktop/pyton/git/prueba-repositorio/proyectodjango/empresa/empresa/plantilla1/miplantilla.html")

	#plt=Template(doc_externo.read())

	#doc_externo.close()

	#ctx=Context({"nombre": p1.nombre, "apellido": p1.apellido, "horario": ahora, "temas": temas_del_curso})

	#{"nombre": p1.nombre, "apellido": p1.apellido, "horario": ahora, "temas": temas_del_curso}documento=doc_externo.render({"nombre": p1.nombre, "apellido": p1.apellido, "horario": ahora, "temas": temas_del_curso})


	return render(request, "miplantilla.html", {"nombre": p1.nombre, "apellido": p1.apellido, "horario": ahora, "temas": temas_del_curso})

def pagina2(request):
	ahora = datetime.datetime.now()

	return render(request, "pagina2.html", {"horario": ahora})

def pagina3(request):
	ahora = datetime.datetime.now()

	return render(request, "pagina3.html", {"horario": ahora})