def CalcularNotaFinalAh():
    #Datos de Entrada
    Unidad1AH=float(input("Ingrese la primera nota Ah: "))
    Unidad2AH=float(input("Ingrese la segunda nota Ah: "))
    Unidad3AH=float(input("Ingrese la tercera nota Ah: "))
    Unidad4AH=float(input("Ingrese la cuarta nota Ah: ")) 
    #proceso
   
    notaAh = Unidad1AH *0.10 + Unidad2AH*0.15+Unidad3AH*0.25+Unidad4AH*0.50
   
    #datos de salida
    print(f"La nota final esAh: {notaAh}")

CalcularNotaFinalAh()