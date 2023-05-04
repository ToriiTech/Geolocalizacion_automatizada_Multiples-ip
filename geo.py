import requests
import signal
import sys
from termcolor import colored

## Funcion para interrupcion del usuario con CTRL+C
def signal_handler(sig, frame):
    print('\nDetenido por el usuario')
    sys.exit(0)

## Asociar la función de manejo de señal a la señal SIGINT (generada por Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

## Verificar que se haya proporcionado el nombre de un archivo de texto con una lista de direcciones IP
if len(sys.argv) < 2:
    print("Solo se ejecutarán archivos con extensión '.txt'")
    sys.exit(1)

## Obtener el nombre del archivo y verificar que tenga la extensión ".txt"
filename = sys.argv[1]
if not filename.endswith(".txt"):
    print("Solo se ejecutarán archivos con extensión '.txt'")
    sys.exit(1)

## Abrir el archivo y procesar cada línea que contenga una dirección IP
with open(filename, 'r') as f:
    for line in f:
        ip = line.strip()
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}")
            response.raise_for_status()
            data = response.json()
            if data["status"] == "success":
                country = data["country"]
                city = data["city"]
                print(f"{colored('[+]', 'green')}  {colored(ip, 'white', attrs=['bold'])} - {colored(country, 'green')} - {colored(city, 'green')}")
            else:
                print(f"{colored('[-]', 'red')}  {colored(ip, 'white', attrs=['bold'])} - {colored('No se pudo obtener la geolocalización', 'red')}")
        except requests.exceptions.RequestException:
            print(f"{colored('[-]', 'red')}  {colored(ip, 'white', attrs=['bold'])} - {colored('No se pudo obtener la geolocalización', 'red')}")
