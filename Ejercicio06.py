### Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
import math
import statistics

def Calculadora_dec_bina ():
    Numero_binario = input('introduce un numero en binario')
    Numero_decimal = int(Numero_binario, 2)
    return (Numero_decimal)
    print (Numero_decimal)
print (Calculadora_dec_bina())
'''Esta funcion lo que hace pasar un numero binario a decimmal, lo primero le pedimos al 
usuario que escriba un numero binario despues creamos una varibale que sera nuestro numero
decimal para luego asignarle que va a ser un numero entero,elegimos la variable de numero binario
y le asginamos tabien una base en este caso dos '''
def Calculadora_bin_dec ():
    Numero_decimal = int(input('Escriba un numero en decimal'))
    Numero_Binario = bin(Numero_decimal)[2:]
    return Numero_Binario
    print (Numero_Binario)
'''En este caso sera al reves le pedimos un numero decimal al usuario que sea entero y despues 
creamos una variable que sea numero binario y pasamos el decimal a binario mediante la funcion bin
y especificamos la base que tenia el numero decimal mediante [2:]
'''
print (Calculadora_bin_dec())