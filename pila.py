
"""una pila representada por listas"""

class Pila(object):
	"""TDA de una pila con listas nativas de python"""
	def __init__(self):
		self.elementos = []
	
	def apilar(self, a_insertar):
		self.elementos.append(a_insertar)
	
	def desapilar(self):
		return self.elementos.pop()
	
	def mostrar(self):
		if len(self.elementos) is 0:
			return 0
		for a in self.elementos:
			print(str(a)+"-->", end=" ")
	def esta_vacia(self):
		return self.elementos == []

