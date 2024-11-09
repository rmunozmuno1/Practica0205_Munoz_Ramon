###Escribir una función que reciba un número entero positivo y devuelva su factorial. Realiza el ejercicio mediante bucles interactivos y mediante una función recursiva.
import math
import statistics
def Factorial ():
    numero = int(input('introduzca un numero entero positivo para realizar el factorial'))
    factorial_nuevo = (math.factorial(numero))
    return factorial_nuevo
'''Realizamos una función donde pedira al usuario meter un numero positivo y entero para que despues devuelva el factorial'''
print (Factorial())
