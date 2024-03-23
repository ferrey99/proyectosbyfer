# Función para calcular el salario bruto
def calcular_salarios(pagaXhora):
    horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: \n"))
    return horas_trabajadas * pagaXhora

# Función para calcular el salario neto
def salario_neto(salario_bruto, aportes_ObraSocial, aportes_Jubilacion):
    # Se descuentan los aportes de la Obra Social y la Jubilación del salario bruto
    return salario_bruto - (salario_bruto * aportes_ObraSocial) - (salario_bruto * aportes_Jubilacion)

# Definimos los valores
pagaXhora = 3200
Aportes_ObraSocial = 0.02  # 2% se representa como 0.02
Aportes_Jubilacion = 0.10  # 10% se representa como 0.10

# Calculamos el salario bruto
salario_bruto = calcular_salarios(pagaXhora)
# Calculamos el salario neto
salario = salario_neto(salario_bruto, Aportes_ObraSocial, Aportes_Jubilacion)

# Imprimimos el salario neto
print("Su sueldo neto a cobrar es ", salario)

if salario_bruto >= 400000:  
    print("Felicidades Ud mantiene al pais en funcionamiento")
else:
    print("Le hace falta currar mas")
