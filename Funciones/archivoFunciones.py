lista = [] 
"""Lista de numeros"""
def lista_principal  (cantidad):
    """LLenar una lista

        :param cantidad de elementos de la lista
        :return Lista
    """
    for i in range (cantidad):
        num = int(input("Digite un número: "))
        lista.append(num)
    return lista
def menor_num (lista):
    """Encuentra el menor numero en una lista
    
        :param lista
        :return EL menor elemento de la lista
    """
    menor = lista[0]
    for i in range(len(lista)):
         if lista[i] < menor:
             menor = lista[i]
    return menor
def mayor_num (lista):
     """Encuentra el mayor numero en una lista
    
        :param lista
        :return EL mayor elemento de la lista
    """
     mayor = lista[0]
     for i in range(len(lista)):
         if lista[i] > mayor:
             mayor = lista[i]
     return mayor
def diferencianum ():
     """Encuentra la diferencia entre
     el mayor y menor numero de una lista
    
        :return La diferencia entre
     el mayor y menor numero de una lista
    """
     mayor = mayor_num(lista)
     menor = menor_num(lista)
     diferencia = mayor - menor
     return diferencia

def diferencia_par(diferencia):
     """Establecesi la diferencia de a y b es par o impar
    
        :param la diferencia
        :return String que confirma o rechaza si el numero es par
    """
     if diferencia % 2 == 0:
         par = ("La diferencia es un numero par")
     else:
         par = ("La diferencia NO es un numero par")
     return par
def cuadrado_list (lista):
    """Eleva al cuadrado los elementos de una lista
    
        :param lista
        :return Segunda lista con los valores elevados al cuadrado
    """
    lista_cuadrada = []
    for i in range (len(lista)):
        cuadrado = lista[i] ** 2
        lista_cuadrada.append(cuadrado)
    return lista_cuadrada
def prom (lista):
    """Establece el promedio de una lista
    
        :param lista
        :return promedio de la lista
    """
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    promedio = suma / len(lista)
    return promedio
def terminanencero (lista):
     """Determina cuantos elementos de la lista
     terminan en 0
    
        :param lista
        :return Cantidad de elementos que termminan en 0
    """
     cont = 0
     for i in range(len(lista)):
         ultimo = lista[i] % 10
         if ultimo == 0:
             cont +=1
     return cont
def digits (lista):
    """Determina los digitos de los numeros de una lista
    
        :param lista
        :return Cantidad de digitos de los numeros de la lista
"""
    digitos = []
    for i in range(len(lista)):
        count = len(str(i))
        digitos.append(count)
    return digitos

def primos(lista):
    """Determina los digitos de los numeros primos de una lista
    
        :param lista
        :return Cantidad de numeros primos de una lista
    """
    primos = []
    for num in lista:
        es_primo = True
        for i in range(2,num):
            if num % i == 0:
                es_primo = False
                break
        if es_primo and num > 1:
            primos.append(num)
    return primos

def main():
    """Funcion principal que llama a otras funciones

    :var nombre asignado para llamar la funcion

    :function funcion a ser llamada

    :args argumentos que utilizan las funciones
    """

    cantidad = 5
    lista_llena = lista_principal(cantidad)
    menor_numi = menor_num(lista)
    mayor_numi = mayor_num(lista)
    diferencia = diferencianum()
    diferencia_pares = diferencia_par(diferencia)
    lista_cuadrada = cuadrado_list(lista)
    promedio = prom(lista)
    cantidadcero = terminanencero(lista)
    digitos = digits(lista)
    prims = primos(lista)
    
    
    print(lista_llena)
    print(menor_numi)
    print(mayor_numi)
    print(diferencia)
    print(diferencia_pares)
    print(lista_cuadrada)
    print(promedio)
    print(cantidadcero)
    print(digitos)
    print(prims)
    """Se imprimen las variables con las funciones asigandas"""
    
if __name__ == '__main__':
    main()
