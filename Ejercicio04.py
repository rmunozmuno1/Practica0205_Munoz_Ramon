### Escribir una función que reciba una muestra de números en una lista y devuelva su media.
#def Lista2 (Numeros):
import math
import statistics
def Lista():
    lista = input('Introduzca los numeros que deses con comas')
    lista = [float(num) for num in lista.split(',')]
    print (statistics.median(lista))
Lista()

