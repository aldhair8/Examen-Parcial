def VacunaparalaspersonasAh():
    # Datos de entrada
    print ("Dime tu nombre: ")
    nombreAh = str (input(" > "))
    print ("Marca 1 = Masculino y 0 = Femenino : ")
    sexoAh = int (input(" > "))
    print ("Dime tu edad: ")
    edadAh = int (input(" > "))
    # Proceso
    if (edadAh > 70):
        print ("Vacuna de tipo [ C ] para " + nombreAh)
    elif (edadAh >= 16 and edadAh <= 69):
        if (sexoAh == 0):
            print ("Vacuna de tipo [ B ] para " + nombreAh)
        elif (sexoAh == 1):
            print ("Vacuna de tipo [ A ] para " + nombreAh)
        else:
            print ("no hay vacuna")
    elif (edadAh < 16):
        print ("Vacuna de tipo [ A ] para " + nombreAh)
    else:
        print ("Vacuna tipo A")
   

VacunaparalaspersonasAh()