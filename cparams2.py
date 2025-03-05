import sys

try:
    if len(sys.argv) == 3:
        num = int(sys.argv[1])  
        print(f"Número de arguments correctes: són {num} i {sys.argv[2]}")
    else:
        print("Número d'arguments incorrecte.")
except ValueError:
    print("Error: El primer argument ha de ser un número.")
finally:
    print("FI")