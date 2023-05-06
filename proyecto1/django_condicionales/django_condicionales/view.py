from django.http import HttpResponse  # Desde django importar http
from datetime import datetime
from django.template import Template, context

def par_impar(request, num):
    if num % 2 == 0:
        par = ('El numero ingresado es par')
    elif num % 2 != 0:
        par = ('El numero ingresado es impar')
    return HttpResponse(par)
def edad(request, edad):
	if edad >= 18:
		mayor =("Usted es mayor de edad, su edad es: ",edad)
	if edad < 18:
		mayor =("Usted no es mayor de edad, su edad es: ",edad)
		return HttpResponse(mayor)

def parque(request, edad_ingreso):
	if edad_ingreso < 4:
		ingreso =("El cliente entra gratis al parque")
	elif edad_ingreso >= 4 and edad_ingreso <= 18:
		ingreso =("El cliente paga 5.000 pesos")
	else:
		ingreso =("Edad invalida")
	return HttpResponse(ingreso)

def sumas(request, num, num2):
	return HttpResponse(num + num2)

def menor(request, num, num2):
	if num < num2:
		menor = num
	else:
		menor = num2
	return HttpResponse(menor)	

def mayor(request, num, num2):
	if num > num2:
		mayor = num
	else:
		mayor = num2
	return HttpResponse(mayor)

def multiplode7 (request, num):
	if num % 7 == 0:
	    multiplo = ('Es multiplo de 7')
	else: 
	    multiplo = ('No es multiplo de 7')
	return HttpResponse(multiplo)
def negativo (request, num):
	if num > 0:
		esnegativo = ("El numero es entero")
	else:
		esnegativo = ("El numero es negativo")
	return HttpResponse(esnegativo)
		
def saludo (request, num):
	if num >= 1 and num  <= 12:
		tipo_saludo = ("Buenos Dìas")
	elif num > 12 and num  <= 18:
		tipo_saludo = ("Buenas Tardes")
	elif num > 18 and num  <= 24:
		tipo_saludo = ("Buenas noches")
	return HttpResponse(tipo_saludo)

def calculadora (request, operador, num, num2):
	if operador == "suma":
		operacion =  ("Suma de ", num ,"+", num2," es: ", num + num2)
	elif operador == "resta":
		operacion =  ("resta de ", num ,"-", num2," es: ", num - num2)
	elif operador == "division":
		operacion =  ("division de ", num ,"/", num2," es: ", num / num2)
	elif operador == "multiplicacion":
		operacion =  ("multiplicacion de ", num ,"*", num2," es: ", num * num2)
	return HttpResponse(operacion)

def terminaen7 (request, num):
	nose = num / 10
	if num % 10 == 7:
		numero = ("termina en 7 ",nose)
	else:
		numero = ("No termina en 7 ",nose)
	return HttpResponse(numero)




	

	

		
    
