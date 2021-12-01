from django.db import models

class Clientes(models.Model):
	nombre = models.CharField(max_length=30)
	direccion = models.CharField(max_length=50)
	email = models.EmailField()
	telefono = models.CharField(max_length=10)

class Articulos(models.Model):
	nombre = models.CharField(max_length=30)
	seccion = models.CharField(max_length=30)
	precio = models.IntegerField()

	def __str__(self):
		return 'El Nombre es %s la dirección es %s y el precio es %s' %(self.nombre, self.seccion, self.precio)

class Pedido(models.Model):
	numero = models.IntegerField()
	fecha = models.DateField()
	entregado =  models.BooleanField()
