#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO
listaNum = []
Verificador = input("¿Vas a querer ingresar un numero?S/N, s/n \n")
while (Verificador == "S" or Verificador == "s"):
    listaNum.append(int(input("Ingrese el numero:")))
    Verificador = input("¿Queres ingresar otro numero a la lista? S/N, s/n \n")


listaNumImpares = []
for i in listaNum:
    if i % 2 != 0:
        listaNumImpares.append(i)

print(listaNum)
print(listaNumImpares)

#FIN