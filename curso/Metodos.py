#metodos
#self se refiere al objeto
#init

class Matematica:
	def suma(self):
		self.n1 = int(input("ingrese un numero: "))
		self.n2 = int(input("ingrese otro numero numero: "))

s = Matematica()
s.suma()
print(s.n1 + s.n2)

class Ropa:
	def __init__(self):
		self.Marca = 'Adida'
		self.talla = 'M'
		self.color = 'Rojo'

remera = Ropa()
print(remera.talla)

class Calculadora:
	def __init__(self, n1, n2):
		self.suma = n1 + n2
		self.resta = n1 + n2
		self.mult = n1 * n2
		self.div = n1 / n2

operacion = Calculadora(n1 = 2, n2 = 3)
print(operacion.suma)



