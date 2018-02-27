#!/usr/bin/python3

import sys


def suma(op1,op2):
	return op1+op2 
def resta(op1,op2):
	return(op1-op2)
def multi(op1,op2):
	return(op1*op2)
def div(op1,op2):
	try:
		return(op1/op2)
	except ZeroDivisionError:
		return('no se puede dividir entre cero')

funciones = { "suma" : suma, "resta" : resta, "multiplicacion" : multi, "division" : div}

if __name__=="__main__":
	
	num_argumento = 4 
	if len(sys.argv) != num_argumento:
		sys.exit("no me has dado todos los argumentos que necesito")
	try:
		oper = sys.argv[1]
		num1 = float(sys.argv[2])
		num2 = float(sys.argv[3])
	except IndexError:
		sys.exit("usage: operador,num1,num2")
	except ValueError:
		sys.exit("num1,num2 tienen que ser numeros")	
	try:
		resultado = funciones [oper] (num1,num2)
	except KeyError:
		sys.exit("no existe la funcion" + operador)	

	print (resultado)
