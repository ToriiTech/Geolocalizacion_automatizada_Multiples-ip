# Geolocalizacion_Automatizada_Multiples-ip
Este script permite obtener la ubicación geográfica de una lista de direcciones IP


## Requerimientos

  - Python 3
  - requests
  - termcolor

## Uso
El script recibe como argumento un archivo de texto con una lista de direcciones IP, una dirección por línea, con la extensión .txt.

El script imprimirá en la consola la ubicación geográfica de cada dirección IP  - país - ciudad. En caso de no poder obtener la ubicación, eviara el correspondiente mensaje de error.

### Ejemplo de uso:

```
[+] python3 geo.py ips.txt

```

