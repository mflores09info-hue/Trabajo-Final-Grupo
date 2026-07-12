#parte 2
def calcular_tarifas_y_sueldos(empLista):
    i = 0
    while i <= (len(empLista) - 1):
        
        # Asignación estricta de tarifa por hora según codRol
        if empLista[i]["codRol"] == 1:
            empLista[i]["tarifa"] = 15
        elif empLista[i]["codRol"] == 2:
            empLista[i]["tarifa"] = 20
        elif empLista[i]["codRol"] == 3:
            empLista[i]["tarifa"] = 25
        elif empLista[i]["codRol"] == 4:
            empLista[i]["tarifa"] = 50
            
        empLista[i]["salBruto"] = (
            (empLista[i]["horasLimNorTotal"] * empLista[i]["tarifa"]) +
            (empLista[i]["horasLimFesTotal"] * empLista[i]["tarifa"] * 1.5) +
            (empLista[i]["horasProNorTotal"] * empLista[i]["tarifa"] * 2) +
            (empLista[i]["horasProFesTotal"] * empLista[i]["tarifa"] * 3) -
            empLista[i]["penalizacion"]
        )

        if empLista[i]["exImpuesto"] == "si":
            empLista[i]["retencion"] = 0
        else:
            empLista[i]["retencion"] = empLista[i]["salBruto"] * 0.08

        # Cálculo de salFinal
        empLista[i]["salFinal"] = empLista[i]["salBruto"] - empLista[i]["retencion"]
        
        i += 1
        
    return empLista