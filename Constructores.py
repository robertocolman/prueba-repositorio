import time
class Persona:
	pass
	def __init__(self, nombre, apellido, año):
		self.nombre = nombre
		self.apellido = apellido
		self.año = año
	def descripcion(self):
		return ' {} {} tiene {}'.format(self.nombre, self.apellido, self.año)
	def comentario(self, frase):
		return ' {} dice: {} '.format(self.nombre, frase)

doctor = Persona('Roberto', 'colman', '27')
print(doctor.descripcion())
time.sleep(1)
print(doctor.comentario('Hasta el amanecer!!'))