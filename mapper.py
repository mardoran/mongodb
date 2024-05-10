import sys
import re
import string

def escribir_ocurrencias():
    # Recorremos cada línea de la entrada
    for linea in sys.stdin:
        # evitamos los retornos de carro
        if linea.isspace():
           continue
        else:
            if linea.startswith("Direc"):
                mac = linea.split()[1]

                # recorremos cada línea cogiendo cada carácter
                print (mac,  1, sep="\t")

if __name__ == "__main__":
    escribir_ocurrencias()