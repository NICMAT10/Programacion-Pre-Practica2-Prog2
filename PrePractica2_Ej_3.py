#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO
from logging import exception

a = int(input("Escribe el primer numero: "))
b = int(input("Escribe el siguiente numero: "))
try:
    c = a / b
    print(c)
    
except ZeroDivisionError as exception:
    print(f"Se ha producido un error | {exception}")
#FIN