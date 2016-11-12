from pila import *

def calculadora_polaca(elementos):
	""" Dada una lista de elementos que representan las componentes de 
	una expresión en notacion polaca inversa, evalúa dicha expresión. 
	Si la expresion está mal formada, levanta ValueError. """
	p = Pila()
	for elemento in elementos:
		try:
			numero = float(elemento)
			p.apilar(numero)
		except ValueError :
			if elemento not in "+-*/ %" or len(elemento) != 1 :
				raise ValueError("operador invalido")
			try:
				a1 = p.desapilar()
				a2 = p.desapilar()
			except ValueError :
				raise ValueError("faltan operandos")
			if elemento == "+":
				print("suma de "+ str(a1)+" "+str(a2))
				resultado = a2 + a1
			elif elemento == "-":
				resultado = a2 - a1
			elif elemento == "*":
				resultado = a2 * a1
			elif elemento == "/":
				resultado = a2 / a1
			elif elemento == " %":
				resultado = a2 % a1
			
			p.apilar(resultado)
			
	res = p.desapilar()
	if p.esta_vacia() :
		return res
	else:
		raise ValueError("sobran elementos en la pila")
def calcular():
	expresion = str(input("ingrese la expresion a evaluar ej : 2 2 + 'dos mas dos' \t ->"))
	elementos = expresion.split()
	print(str(calculadora_polaca(elementos) ))
	

