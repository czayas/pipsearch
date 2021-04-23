# pipsearch
Alternativa al comando 'pip search' que está siendo descontinuado por sus desarrolladores.

La opción de búsqueda de pip consulta a los servidores de PyPI (Python Package Index) cuyos mantenedores han explicado que dicha llamada de la API consume muchos recursos y es demasiado costosa para mantenerla abierta al público. En consecuencia, planean eliminarla por completo pronto.

Una alternativa consiste en realizar la búsqueda directamente en la web de PyPI (https://pypi.org) y copiar y pegar la sentencia de instalación del paquete deseado en la consola.

Este script ofrece otra alternativa, accesible desde consola:

```bash
$ ./pipsearch.py [palabra clave]
```

Happy hacking!
