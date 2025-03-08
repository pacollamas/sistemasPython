try:
    with open('fitxer01.txt', 'r') as file:
        lines = file.readlines()
    try:
        for i, line in enumerate(lines):
            if i % 2 == 0:  
                print(line.strip())
    except Exception as e:
        print(f"Error: {e}")

except FileNotFoundError as e:
    print(f"Error en abrir el archivo:{e}")
finally:
    print("Fin del programa")