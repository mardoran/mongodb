import sys
import re
import string

def escribir_ocurrencias():
    # Recorremos cada línea de la entrada
    for linea in sys.stdin:
        # evitamos las líneas en blanco
        if linea.isspace():
           continue
        else:
            #si la línea comienza por Direc (esquivamos el acento para ahorranos problemas)
            if linea.startswith("Direc"):
                #cogemos la parte de la mac
                mac = linea.split()[1]
                # escribimos la mac y 1 por cada ocurrencia
                print (mac,  1, sep="\t")

if __name__ == "__main__":
    escribir_ocurrencias()