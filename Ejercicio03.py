### Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
import math
'''Importamos la biblioteca Math para el numero PI'''
def Area(radio):
    '''Definimos la funcion Area para '''
    AreaR= (math.pi * (radio)**2)
    '''Realizamos una variable con la operacion para sacar el Area'''
    return AreaR
    '''Usamos el return para guardar el resultado'''
print (Area(5))
'''Imprimimos para consultar si funciona'''
def Volumen_cilidro(altura):
    '''Definimos el volumen donde necesitamos la altura'''
    print (Area(5) * altura)
    '''Imprimimos para realizar la operación'''
    return Volumen_cilidro
print (Volumen_cilidro(5))
