from django.http import HttpResponse  # Desde django importar http
from django.template import Template, context
import random

def numeros_al_10 (request, num):
    lista = []
    if num < 10:
        for i in range(num,10):
            lista.append(i)
    elif num > 10:
        for i in range(10,num,):
            lista.append(i)
    return HttpResponse(lista)

def numeros_al_10_2 (request, inicio, limite):
    lista = []
    for i in range(inicio,limite+1):
        lista.append(i)
    return HttpResponse(lista)

def pares_al_10 (request, num):
    lista = []
    for i in range(1,num,2):
        lista.append(i)
    return HttpResponse(lista)
    
def caracteres (request, texto):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    listai = []
    
    for e in range(len(texto)):
        if texto[e] == "a":
            a+=1
        elif texto[e] == "e":
            e+=1
        elif texto[e] == "i":
            i+=1
            listai.append(i)
        elif texto[e] == "o":
            o+=1
        elif texto[e] == "u":
            u+=1
    vocales= ("La cantidad de vocales que tiene su texto es  a = ",a," ,e = ",e,", i = " ,i," ,o =  ",o," ,u =  ",u)
    return HttpResponse(vocales)

def es_primo(request,num):
    for n in range(2, num):
        divisor = 0
        if num % n == 0:
            es_divisible = False
            divisor = n
            break
        else:
            es_divisible = True
    if es_divisible:
        mensaje = "Es primo"    
    else:
        mensaje = "No es primo, " + str(divisor) + " es divisor"
    return HttpResponse(mensaje)

def Generar_sumatoria(request, limite):
    suma = 0
    for i in range(1,limite):                              
        suma += i
    return HttpResponse(suma)


def Generar_promedio(request, limite):
    suma = 0
    for i in range(1,limite):                              
        suma += i
        prom = suma / limite
    return HttpResponse(prom)

def palindromo (request, palabra):
    palabra_al_reves = ""
    for i in range(len(palabra)-1, -1, -1):
        palabra_al_reves += palabra[i]
    if palabra_al_reves ==  palabra:
        condicion = ("La palabra es palindroma")
    else:
        condicion = ("La palabra NO es palindroma")
    return HttpResponse(condicion)

def div_exacta(request,num):
    exactos = []
    for n in range(1, num):
        if num % n == 0:
            exactos.append(n)
    return HttpResponse(exactos)

def termina_4(request,inicial, numero):
     
def entredigitos(request,num):
    entre = []
    if num > 9 and num < 100:
        digito1 = num // 10
        digito2 = num % 10
        for i in range (digito1, digito2):
            entre.append(i)
    return HttpResponse(entre)

def entredigitos_pares(request,num):
    pares = []
    if num > 9 and num < 100:
        digito1 = num // 10
        digito2 = num % 10
        for i in range (digito1, digito2):
            if i % 2 == 0:
                pares.append(i)
    return HttpResponse(pares)

# def tabla(request,num): 
#         for i in range(1,11):
#             tablas = num * i
#             tabla =(num ,"*", i ," = ",tablas)
#         return HttpResponse(tabla)

    



