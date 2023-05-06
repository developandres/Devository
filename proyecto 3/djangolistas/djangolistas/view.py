from django.http import HttpResponse  # Desde django importar http
from django.template import Template, context
import random

# def lista(request):
#     lista = []
#     for i in range(10):
#         numeros = random.randint(1,100)
#         lista.append(numeros)
#     return HttpResponse(lista)

lista = []
for i in range(11):
    numeros = random.randint(-9999,9999)
    lista.append(numeros)
     
def ex1 (request):
    mayor = max(lista)
    return HttpResponse(mayor)

def ex2 (request):
    menor = min(lista)
    return HttpResponse(menor)

def ex3 (request):
    mayor_par = max(filter(lambda x : x % 2 == 0, lista ))
    return HttpResponse(mayor_par)

def ex4 (request, limite):
    fib = [0,1]
    for i in range (2,limite):
        siguiente = fib [-1] + fib [-2]
        fib.append(siguiente)
    return HttpResponse(fib)

# def ex4(request, limite):
#     fib = [0, 1] + [fib[i-1] + fib[i-2] for i in range(2, limite)]
#     return HttpResponse(fib)
     
def ex5 (request):
    mayor = lista[0]
    for i in range (len(lista)):
        if lista[i] > mayor:
            ambos = ("Posicion: ",lista[i]," valor: ", i)
    return HttpResponse(ambos)

def ex6 (request):
    termina4 = []
    for i in range(len(lista)):
        if i % 10 == 4:
            termina4.append(i)
    return HttpResponse(termina4)

def ex7 (request):
    cont = 0
    num = []
    for i in range (len(lista)):
        if  lista [i] < 100:
            cont +=1
            num.append(i)
        cantidad = ("La cantidad de numeros con menos de 2 digitos son: ",cont," y son: ",num)
    return HttpResponse(cantidad)

def ex8 (request):
    nums = []
    posis = []
    for i in range (len(lista)):
        if  lista [i] >= 100:
            posis.append(lista[i])
            nums.append(i)
            tupla1 = '(' + ', '.join(str(x) for x in nums) + ')'
            tupla2 = '(' + ', '.join(str(x) for x in posis) + ')'
            mensaje = f"Las posiciones de los números con más de 3 dígitos son: {tupla1} y sus valores son: {tupla2}"
    return HttpResponse(mensaje)

def ex9(request):
    prom = int(sum(lista) / (len(lista)))
    return HttpResponse(prom)

def ex10(request):
    valor = False
    promedio = int(sum(lista) / (len(lista)))
    for i in range (len(lista)):
        if promedio == lista[i]:
            valor = True
            break
    return HttpResponse(valor)

def ex11(request):
    cont = 0
    valores = []
    for i in range (len(lista)):
        if lista[i] % 3 == 0:
            cont +=1
            valores.append(lista[i])
            tupla_valores = '(' + ', '.join(str(x) for x in valores) + ')'
        mensaje = ("La cantidad de numeros multiplos de 3 de la lista son:" , cont , " y sus valores son: ", tupla_valores)
    return HttpResponse(mensaje)

def ex12 (request):
    cont = 0
    minus = []
    for i in range (len(lista)):
        if lista[i] < 0:
            cont +=1
            minus.append(lista[i])
            tupla1 = '(' + ', '.join(str(x) for x in minus) + ')'
        mensaje = ("La cantidad de numeros negativos son:" , cont , " y sus valores son: ", minus)
    return HttpResponse(mensaje)





