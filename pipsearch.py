#!/usr/bin/env python3
'''
pipsearch - Reemplazo de la opción de búsqueda del administrador de paquetes de
            Python (pip) que está siendo descontinuada por los mantenedores.

La opción de búsqueda de pip consulta a los servidores de PyPI (Python Package
Index) cuyos mantenedores han explicado que dicha llamada de la API consume
muchos recursos y es demasiado costosa para mantenerla abierta al público. En
consecuencia, planean eliminarla por completo pronto.

Una alternativa consiste en realizar la búsqueda directamente en la web de PyPI,
y copiar y pegar la sentencia de instalación del paquete deseado en la consola.

Python Package Index: https://pypi.org/

Este script ofrece otra alternativa, accesible desde consola. Happy hacking!

Programado por Carlos Zayas <czayas en gmail> 23/04/2021
'''

import sys
import urllib.request

if len(sys.argv) > 1:     # Si se invoca el programa con al menos un parámetro...
    buscado = sys.argv[1] # Se toma el primero (el índice 0 es el programa)
else:
    buscado = ''
request = urllib.request.Request('https://pypi.org/simple/') # Repositorio PIP
pagina = urllib.request.urlopen(request).read().decode('utf8')
for linea in pagina.split('\n'):
    if 'a href' in linea:
        paquete = linea.split('/')[2] # Se toma el nombre del paquete (índice 2)
        if (buscado in paquete) or not buscado:
            print(paquete)
