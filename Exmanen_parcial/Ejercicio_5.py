def algoritmo5Dpl():
    # Datos de entrada
    print ("Cauanto es tu salario: ")
    salarioAh = int (input (" > "))
    # Proceso
    print ("Año " + " : " + " Salario")
    salarioIncrementoAh = salarioAh * 0.10
    for incrementoAh in range(1, 7):
        salarioAh = salarioIncrementoAh + salarioAh
        print(incrementoAh , "   :  ", salarioAh)
    print("Gracias....")
algoritmo5Dpl()
