import sys
import re
import string
from unidecode import unidecode

def normalizar_texto(texto):
    # Utilizamos una expresión regular para mantener solo letras 
    texto_normalizado = re.sub(r'[^a-zA-Z]', '', texto)
    return texto_normalizado

def escribir_ocurrencias():
    # Recorremos cada línea de la entrada
    for linea in sys.stdin:
        # la función unidecode elimina los acentos y similares pasando todos los caracteres a ASCII
        #linea = unidecode(linea)    

        #la función unicode da un error en el fichero portugués así que la hemos cambiado por esta    
        linea = normalizar_texto(linea)
        
        # convertimos toda la línea a minúsculas para no diferenciar
        linea = linea.lower()
        # recorremos cada línea cogiendo cada carácter
        for caracter in linea:
            # verificamos si el carácter es una letra del alfabeto con la función isalpha
            if caracter.isalpha():
                # escribimos la letra y un 1 para cada ocurrencia
                print (caracter,  1, sep="\t")

if __name__ == "__main__":
    escribir_ocurrencias()
