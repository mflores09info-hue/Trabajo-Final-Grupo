
import os

def registrar_personal():
    empLista = []
    
    print("REGISTRO DE PERSONAL - KAMELI SERVICIOS")
    
    while True:
        desea_ingresar = input("¿Deseas ingresar un nuevo empleado (si/no)?: ").strip().lower()
        if desea_ingresar != "si":
            break
            
        nomCompleto = input("Nombre completo del empleado: ").strip()
        
        print("")
        print("Código de Rol:")
        print("1. Ayudante (S/. 15.00/h)")
        print("2. Técnico (S/. 20.00/h)")
        print("3. Supervisor (S/. 25.00/h)")
        print("4. Supervisor SSOMA (S/. 50.00/h)")
        
        while True:
            try:
                codRol = int(input("Ingrese el código del rol: "))
                if codRol in [1, 2, 3, 4]:
                    break
                print("ingrese un número del 1 al 4")
            except ValueError:
                print("Por favor, ingrese un número entero válido")
        
        try:
            horasLimNorTotal = float(input("Total de horas trabajadas en Lima NO festivas: "))
            horasLimFesTotal = float(input("Total de horas trabajadas en Lima festivas: "))
            horasProNorTotal = float(input("Total de horas trabajadas en Provincia NO festivas: "))
            horasProFesTotal = float(input("Total de horas trabajadas en Provincia festivas: "))
            
            exImpuesto = input("¿El empleado cuenta con exoneración de 4ta categoría (si/no)?: ").strip().lower()
            penalizacion = float(input("Penalización por daños de herramientas (inserte el monto): "))
        except ValueError:
            print("ErrorSe reiniciará el registro de este empleado")
            print("")
            continue

        empleado = {
            "nomCompleto": nomCompleto,
            "codRol": codRol,
            "horasLimNorTotal": horasLimNorTotal,
            "horasLimFesTotal": horasLimFesTotal,
            "horasProNorTotal": horasProNorTotal,
            "horasProFesTotal": horasProFesTotal,
            "exImpuesto": exImpuesto,
            "penalizacion": penalizacion
        }
        
        empLista.append(empleado)
        print("Se registo al empleado!\n" + "-"*50)
            
    return empLista

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
        empLista[i]["salFinal"] = empLista[i]["salBruto"] - empLista[i]["retencion"]
        i += 1
        
    return empLista
#parte 3
def generar_reporte(empListaProcesada):
    lineas_reporte = []
    lineas_reporte.append("      REPORTE DE PLANILLA - KAMELI SERVICIOS ")

    for emp in empListaProcesada:
        detalle = (
            f"Empleado: {emp['nomCompleto']}\n"
            f"Código de Rol: {emp['codRol']} (Tarifa asignada: S/. {emp['tarifa']:.2f}/h)\n"
            f"Horas Totales:\n"
            f"  - Lima Normal: {emp['horasLimNorTotal']} | Lima Festiva: {emp['horasLimFesTotal']}\n"
            f"  - Prov. Normal: {emp['horasProNorTotal']} | Prov. Festiva: {emp['horasProFesTotal']}\n"
            f"Descuento por Penalización: S/. {emp['penalizacion']:.2f}\n"
            f"--------------------------------------------------\n"
            f"Salario Bruto Calculado: S/. {emp['salBruto']:.2f}\n"
            f"Retención 4ta Categoría: S/. {emp['retencion']:.2f}\n"
            f"SALARIO FINAL NETO: S/. {emp['salFinal']:.2f}\n"
        )
        lineas_reporte.append(detalle)

    reporte_completo = "\n".join(lineas_reporte)
    print(reporte_completo)

    nombre_archivo = "reporte_pagos_kameli.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(reporte_completo)
        
    print(f"✅ ¡Éxito! El reporte se guardó en: '{os.path.abspath(nombre_archivo)}'")

if __name__ == "__main__":
    lista_cruda = registrar_personal()
    
    if lista_cruda:
        lista_calculada = calcular_tarifas_y_sueldos(lista_cruda)
        generar_reporte(lista_calculada)
    else:
        print("No se registraron empleados en el sistema.")