
=======
import os

#REGISTRO DE PERSONAL
def registrar_personal():
    empLista = []
    
    print("REGISTRO DE PERSONAL - KAMELI SERVICIOS")
    
    while True:
        # Pregunta si desea ingresar un nuevo empleado
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

>>>>>>> 928bb8900aff9f855198adc11f7bafb261ab5412
<<<<<<< HEAD
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

        # Cálculo de salFinal
        empLista[i]["salFinal"] = empLista[i]["salBruto"] - empLista[i]["retencion"]
        
        i += 1
        
    return empLista<<<<<<< HEAD
