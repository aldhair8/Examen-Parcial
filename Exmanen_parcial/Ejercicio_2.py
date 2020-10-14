def AumentoaProfesoresAh():
    #Datos de Entrada
    salaMin=1247
    puntos1Ah= int(input("Ingrese la cantidad de puntos:"))

    if(puntos1Ah>=50 <=100):
            salaMin+= salaMin+(salaMin*0.1)
            print("el salarios es:", salaMin)
    elif (puntos1Ah>=101 <=150):
        salaMin2= salaMin+(salaMin*0.5)
        print("el salarios es:", salaMin2)
    else:
        salaMin3= salaMin+(salaMin*0.8)
        print("el salario es:", salaMin3)
    
            
        
    
    

AumentoaProfesoresAh()