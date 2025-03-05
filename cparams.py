import sys    

try:
    if len(sys.argv) == 3:
        print(f"Numero de argumentos correctos: són {sys.argv[1]} y {sys.argv[2]} ")
    else: 
        print("Numero de argunmentos equivocado")
except ValueError as e:
    print(f"{e}")
finally:
    print("FI")