from django.http import HttpResponse  # Desde django importar http
from django.template import Template, context
import random
def ex1(request):
    matriz = []
    mayor = 0
    contador = 0
    tamaño = 4
    for i in range(tamaño):
        lista = []
        for j in range(tamaño):
            # numero = int(input("Digite un numero: "))
            numero_aleatorio = random.randint(1, 10)
            lista.append(numero_aleatorio)
            if numero_aleatorio > mayor:
                mayor = numero_aleatorio
            elif numero_aleatorio == mayor:
                contador+=1
        matriz.append(lista)
    mensaje=f"El mayor numero ingresado es: { mayor }.Matriz:  { matriz }"
    return HttpResponse(mensaje)
def ex2(request):
    matriz = []
    mayor = 0
    contador = 0
    tamaño = 4
    for i in range(tamaño):
        lista = []
        for j in range(tamaño):
            # numero = int(input("Digite un numero: "))
            numero_aleatorio = random.randint(1, 10)
            lista.append(numero_aleatorio)
            if numero_aleatorio > mayor:
                mayor = numero_aleatorio
            elif numero_aleatorio == mayor:
                contador+=1
        matriz.append(lista)
    mensaje=f"El mayor se repite: { contador }.Matriz:  { matriz }"
    return HttpResponse(mensaje)
def ex3(request):
    matriz = []
    pares = []
    posi_pares = []
    for i in range(3):
        lista = []
        for j in range(4):
            # numero = int(input("Digite un numero: "))
            numero_aleatorio = random.randint(1, 10)
            lista.append(numero_aleatorio)
            if numero_aleatorio % 2 == 0:
                pares.append(numero_aleatorio)
                posi_pares.append((i,j))
        matriz.append(lista)
    mensaje=f"Los pares son: { pares }, sus posiciones son:  { posi_pares }.Matriz:  { matriz }"
    return HttpResponse(mensaje)
def ex4(request):
    matriz = []
    primos = []
    posi_primos = []
    for i in range(4):
        lista = []
        for j in range(3):
            cont = 0
            numero_aleatorio = random.randint(1, 10)
            lista.append(numero_aleatorio)
            for y in range(2,numero_aleatorio):
                if numero_aleatorio % y == 0:               
                    cont +=1     
            if cont == 0:
                cont +=1     
                primos.append(numero_aleatorio)
                posi_primos.append((i,j))
        matriz.append(lista)
    mensaje=f"Los primos son: { primos }, sus posiciones son:  { posi_primos }.Matriz:  { matriz }"
    return HttpResponse(mensaje)
def ex5(request):
    matriz = []
    for i in range(4):
        lista = []
        for j in range(3):
            numero_aleatorio = random.randint(1, 10)
            lista.append(numero_aleatorio)
        matriz.append(lista)

    sumatorias = []
    for fila in matriz:
        suma_fila = sum(fila)
        sumatorias.append(suma_fila)

    mayor = max(sumatorias)
    posi = sumatorias.index(mayor)

    mensaje = f"La fila con la mayor sumatoria es: {posi+1}, su valor es: {mayor}. Matriz: {matriz}"
    print(mensaje)
    return HttpResponse(mensaje)
def ex6(request):
    matriz = []
    contador = 0
    en0 = []
    for i in range(4):
        lista = []
        for j in range(4):
            numero_aleatorio = random.randint(1, 50)
            lista.append(numero_aleatorio)
            if numero_aleatorio % 10  == 0:
                contador +=1
                en0.append(numero_aleatorio)
        matriz.append(lista)
        mensaje = f"Cantidad de numeros que terminan en 0: {contador}, son: {en0}. Matriz: {matriz}"
    return HttpResponse(mensaje)
def ex7(request):
    matriz = []
    lista_primos = []
    cont = 0     
    max_primo = 0

    for q in range(5):
        lista = []
        for w in range(3):
            cont = 0     
            numero_aleatorio = random.randint(1, 10)
            lista.append(numero_aleatorio)
            for y in range(2,numero_aleatorio):
                if numero_aleatorio % y == 0:               
                    cont +=1     
            if cont == 0:    
                lista_primos.append(numero_aleatorio)
                max_primo = max(lista_primos)
        matriz.append(lista)
    mensaje = f"El numero mayor primo de la matriz es: {max_primo}. Matriz: {matriz}"
    return HttpResponse(mensaje)
def ex8(request):            
    matriz = []
    tamaño = 4
    contador = 0

    for q in range(tamaño):
        lista = []
        for w in range(tamaño):
            numero_aleatorio = random.randint(1, 1000)
            lista.append(numero_aleatorio)
            if numero_aleatorio > 99 and numero_aleatorio < 1000:
                contador += 1
        matriz.append(lista)
    mensaje = f"La cantidad de numeros con mas 3 digitos: {contador}. Matriz: {matriz}"
    return HttpResponse(mensaje)
def ex9(request):            
    matriz = []
    tamaño = 4
    contador = 0

    for q in range(tamaño):
        lista = []
        for w in range(tamaño):
            numero_aleatorio = random.randint(1, 1000)
            lista.append(numero_aleatorio)
            if numero_aleatorio > 0 and numero_aleatorio < 10:
                contador += 1
        matriz.append(lista)
    mensaje = f"La cantidad de numeros con 1 digito es : {contador}. Matriz: {matriz}"
    return HttpResponse(mensaje)

def ex10(request):            
    matriz = []
    menor = 0
    contador = 0

    for q in range(4):
        lista = []
        for w in range(6):
            contador = 0
            numero_aleatorio = random.randint(1, 1000)
            lista.append(numero_aleatorio)
            menor = min(lista)
            if menor == numero_aleatorio:
                contador +=1
        matriz.append(lista)

    mensaje = f"El menor elemento de la lista es : {menor}, y se repite {contador}. Matriz: {matriz}"
    return HttpResponse(mensaje)

def ex11(request):            
    matriz = []
    sumatoria = 0
    for q in range(4):
        lista = []
        for w in range(6):
            contador = 0
            numero_aleatorio = random.randint(1, 1000)
            lista.append(numero_aleatorio)
            sumatoria = sum(lista)
            prom = int(sumatoria / (len(lista)))
        matriz.append(lista)    
    mensaje = f"Promedio de la lista es: {prom}. Matriz: {matriz}"
    return HttpResponse(mensaje)

def ex12(request):            
    matriz = []
    sumatoria = 0
    en_la_matriz = ("el promedio No se encentra en la matriz")
    for q in range(4):
        lista = []
        for w in range(6):
            numero_aleatorio = random.randint(1, 5)
            lista.append(numero_aleatorio)
            sumatoria = sum(lista)
            prom = int(sumatoria / (len(lista)))
            if prom == numero_aleatorio:
                en_la_matriz = ("el promedio se encentra en la matriz")
        matriz.append(lista)    
    mensaje = f"Promedio de la lista es: {prom},{en_la_matriz}.  Matriz: {matriz}"
    return HttpResponse(mensaje)
