import sys

try:
    if len(sys.argv) == 3:
        num = int(sys.argv[1])  
        print(f"Número de argumentos correctos: son {num} y {sys.argv[2]}")
    else:
        print("Número de argumentos incorrecto.")
except ValueError:
    print("Error: El primer argumento debe ser un número.")
finally:
    print("FIN")