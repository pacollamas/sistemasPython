import random

valor=random.randint(1, 100)
x = 0
intents=0
continuar=True
print(valor)
try:
    while continuar:
        try:
            numero = int(input("Introdueix un número aleatori: "))
            intents += 1
            if numero < valor:
                print("El número és més gran.")
            elif numero > valor:
                print("El número és més petit.")
            else:
                print(f"Has encertat el número en {intents} intents.")
                continuar=False
        except ValueError as e:
            print(f"Introduiex un nuemro vàlid:{e}")
finally:
    print("FI del joc!!!!!")