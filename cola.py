class Cola(object):
	def __init__(self):
		self.elementos = []
		
	def encolar(self, elemento):
		self.elementos.append(elemento)
	
	def desencolar(self):
		if self.elementos is [] :
			return None
			
		else:
			#pass
			return self.elementos.pop(0)
		
	def esta_vacia(self):
		return self.elementos is []
	
	def mostrar(self):
		for i in self.elementos:
			print(str(i)+"--> ", end="" )
