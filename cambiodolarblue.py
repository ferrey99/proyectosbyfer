 # establecer valor dolar blue
Dolar_Blue = int ("1040")
print("El valor del Dolar Blue es de: ", Dolar_Blue)
# Calcular el cambio que se debe dar para tener una cantidad de pesos igual a los dólares.
pesos =  int(input("Ingrese la cantidad  de Pesos que desea convertir a  Dolares: "))
dolares = pesos / Dolar_Blue
print ("Cantidad de Dolares equivalente a :" + str(dolares, ) ) 
 #redondear el valor  a dos decimales y mostrarlo en pantalla.
def  redondeo (dolares):   
    return round(dolares,2)  
resultado=redondeo(dolares)
print (resultado)      