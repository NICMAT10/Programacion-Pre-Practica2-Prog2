#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO
lista1=[]
cierre=0
y=0
maximo=0
z=5000
for x in range(z):
    print("Ingrese un elemento de la lista")
    lista1.append(int(input()))
    maximo=max(lista1[y],maximo)
    print(f"El numero maximo es {maximo}")
    y=y+1
    print("Desea ingresar otro numero?")
    cierre=str(input())
    if cierre != "si" and cierre != "Si":
        break
print(f"El maximo numero registrado es {maximo}")
#FIN