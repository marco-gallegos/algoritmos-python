from pila import *
from calculadora_polaca import *
from cola import *
from colaenlazada import *

stk = Pila()
que = Cola()
que_crazy = Cola_loca()
while 1:
	opc = int(input("1 - pila ** 2 - cola ** 3 - calculadora polaca ** 4 - cola enlazada\n -> "))
	opc2 = 0
	if opc is 1:
		while opc2 != 6 :
			opc2 = int(input("1 - agregar ** 2 - eliminar ** 3 - mostrar \n -> "))
			if opc2 is 1 :
				insertar = int(input("dame un numero -> "))
				stk.apilar(insertar)
			elif opc2 is 2 :
				print("elimine -> "+str(stk.desapilar()))
			elif opc2 is 3 :
				stk.mostrar()
				print()
		opc2 = -1
		
		
	elif opc is 2 :
		while opc2 != 6:
			opc2 = int(input("1 - agregar ** 2 - eliminar ** 3 - mostrar \n -> "))
			if opc2 is 1 :
				insertar = int(input("dame un numero -> "))
				que.encolar(insertar)
			elif opc2 is 2 :
				print("elimine -> "+str(que.desencolar()))
			elif opc2 is 3 :
				que.mostrar()
				print()
		opc2 = -1	
	
	
	elif opc is 3 :
		while opc2 != 6:
			opc2 = int(input("1 usar ** 6 salir -> "))
			if opc2 is 1:
				calcular()
		opc2 = -1
		
		
	elif opc is 4:
		while opc2 != 6:
			opc2 = int(input("1 - agregar ** 2 - eliminar ** 3 - mostrar \n -> "))
			if opc2 is 1 :
				insertar = int(input("dame un numero -> "))
				que_crazy.encolar(insertar)
			elif opc2 is 2 :
				print("elimine -> "+str(que_crazy.desencolar()))
			elif opc2 is 3 :
				que_crazy.mostrar()
				print()
		opc2 = -1
			
