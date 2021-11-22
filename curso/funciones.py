class Persona:
	edad = 27
	nombre = 'Roberto'

doctor = Persona()
print('la edad de la persona es:',Persona.nombre)
print('la edad de la persona es:', getattr(doctor, 'edad'))
print('el doctor tiene una edad?', hasattr(doctor, 'edad'))
setattr(doctor, 'nombre', 'Robert')
print(doctor.nombre)