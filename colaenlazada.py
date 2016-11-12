class Nodo(object):
	def __init__(self,dato = None,sig = None ):
		self.dato = dato
		self.siguiente = sig

	def __str__(self):
		return str(self.dato)

class Cola_loca(object):
	"""cola utilizando nodos"""
	def __init__(self):
		self.raiz = None
	
	def __len__(self):
		if self.raiz is None :
			return 0
		numero_nodos = 0
		auxiliar = self.raiz
		numero_nodos += 1
		while auxiliar.siguiente is not None :
			numero_nodos += 1
		return numero_nodos
	
	def encolar(self, dato):
		if self.raiz is None :
			self.raiz = Nodo(dato)
		else :
			auxiliar = self.raiz
			while auxiliar.siguiente is not None :
				auxiliar = auxiliar.siguiente
			
			auxiliar.siguiente = Nodo(dato)
	
	def desencolar(self):
		auxiliar = self.raiz
		if auxiliar is None :
			return
		dato = self.raiz.dato
		self.raiz = self.raiz.siguiente
		del auxiliar
		return dato

	def mostrar(self):
		if self.raiz is None :
			return
		auxiliar = self.raiz
		
		print(str(auxiliar.dato)+" --> ", end="")
		while auxiliar.siguiente is not None :
			auxiliar = auxiliar.siguiente
			print(str(auxiliar.dato)+" --> ", end="")
			
		
