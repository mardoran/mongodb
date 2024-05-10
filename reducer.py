import sys

contador = 0
mac_anterior = None
for linea in sys.stdin:
    lista = linea.split("\t")
    mac = lista[0]
    #lo siguiente no es necesario porque sabemos que siempre va a ser 1
    #recuento = lista[1]
    #mac, recuento = linea.split("\t")

    #si la variable mac_anterior es nula estamos en primera línea del bucle así que la inicializamos
    #con la primera mac
    if mac_anterior == None:
        mac_anterior = mac
    #si la mac es igual a la anterior vamos sumando
    if mac == mac_anterior:
        contador += 1
    #como el archivo está ordenado cuando no sea igual es que cambiamos de mac
    #así que imprimimos el recuento total
    else:
        print(mac_anterior, contador, sep="\t")
        #como ya hemos leído una nueva mac la guardamos en la variable mac_anterior para comparar
        #y inicializamos el contador a 1 porque ya hemos leído una ocurrencia
        mac_anterior = mac
        contador = 1
#si se acaba el bucle es que habremos llegado a la última fila y tenemos que mostrar la última mac
print(mac_anterior, contador, sep="\t")