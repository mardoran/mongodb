import sys

contador = 0
letra_anterior = None
for linea in sys.stdin:
    linea = linea.strip()
    lista = linea.split("\t")
    letra = lista[0]
    #lo siguiente no es necesario porque sabemos que siempre va a ser 1
    #recuento = lista[1]
    #letra, recuento = linea.split("\t")

    #si la variable letra_anterior es nula estamos en primera línea del bucle así que la inicializamos
    #con la primera letra
    if letra_anterior == None:
        letra_anterior = letra
    #si la letra es igual a la anterior vamos sumando
    if letra == letra_anterior:
        contador += 1
    #como el archivo está ordenado cuando no sea igual es que cambiamos de letra
    #así que imprimimos el recuento total
    else:
        print(letra_anterior, contador, sep="\t")
        #como ya hemos leído una nueva letra la guardamos en la variable letra_anterior para comparar
        #y inicializamos el contador a 1 porque ya hemos leído una ocurrencia
        letra_anterior = letra
        contador = 1
#si se acaba el bucle es que habremos llegado a la última fila y tenemos que mostrar la última letra
print(letra_anterior, contador, sep="\t")