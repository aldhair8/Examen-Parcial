def AumentoaProfesoresAh():
     #Datos de Entrada
     salaMin= int(input("Dime tu salario: "))
     puntos1Ah= int(input("Ingrese la cantidad de puntos:"))

     if(puntos1Ah>=50 and puntos1Ah <=100):
         salaMin+= salaMin* 0.1
         print("el salarios de 50:", salaMin)
     elif (puntos1Ah>=101 and puntos1Ah <=150):
         salaMin2= (salaMin)+(salaMin*0.5)
         print("el salarios es 101 >:", salaMin2)
     elif (puntos1Ah >= 151):
         salaMin3= (salaMin)+(salaMin*0.8)
         print("el salario es:", salaMin3)
     else:
         print("Tu salario es :", salaMin)
AumentoaProfesoresAh()