def CalcularvaloresaritmeticosAh():
    # Dato de entrada
    print ("""Que operacion aritmetica aras:
    \n1. [+]
    \n2. [-]
    \n3. [*]
    \n4. [/]
    \n5. [**]
    \n
    """)
    signoAh = int (input (" > "))
    print ("Cual es el valor a: ")
    aAh = int (input(" > "))
    print("Cual es el valor b: ")
    bAh = int (input(" > "))
    # Proceso
    if signoAh == 1:
        operacionAh = aAh + bAh
    elif signoAh == 2:
        operacionAh = aAh - bAh
    elif signoAh == 3:
        operacionAh = aAh * bAh
    elif signoAh == 4:
        operacionAh = aAh / bAh
    elif signoAh == 5:
        operacionAh = aAh**bAh
    else:
        print ("No hay mas")
    print ("el resultado es:", operacionAh)

CalcularvaloresaritmeticosAh()