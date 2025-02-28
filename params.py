import sys    # per importar la llibreria necessària

florin=(len(sys.argv))
print(florin)
num=1
if(len(sys.argv) > 1):
    while num < florin:
        for x in sys.argv[num] :
            print(x)
            num+=1
    print(f"Obrint {sys.argv}")   


else:
    print("Has d’indicar el nom de l’arxiu")

       # si el nombre de paràmetres és superior a 1. és a dir, n’hi han

       # et mostra el primer paràmetre