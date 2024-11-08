### Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus valores al cuadrado.
import statistics
import math
def lista_numeros():
    numeros = input('Introduce los numeros que quieras elevar al cuadrado separados con coma')
    numeros = [float(num) for num in numeros.split(',')]
    return numeros
def numeros_al_cuadrado(numeros):
    Numeros_elevado_a_dos = [num ** 2 for num in numeros]
    return Numeros_elevado_a_dos
Numeros = lista_numeros()
resultado = numeros_al_cuadrado(Numeros)
print (resultado)

