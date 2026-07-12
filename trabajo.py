# ==========================================
# TRABAJO FINAL - PROGRAMACIÓN BÁSICA
# ==========================================

# --- PARTE 1 (Compañero 1) ---
def parte_uno_registro():
    print("--- MÓDULO DE REGISTRO (En desarrollo) ---")
    # Tu compañero de la Parte 1 programará su lógica aquí dentro
    pass


# --- PARTE 2 (Compañero 2) ---
def parte_dos_gestion():
    print("--- MÓDULO DE GESTIÓN (En desarrollo) ---")
    # Tu compañero de la Parte 2 programará su lógica aquí dentro
    pass


# --- PARTE 3: REPORTE (Tu Parte) ---
def parte_tres_reporte():
    print("====================================")
    print("        REPORTE GENERAL - HU-03      ")
    print("====================================")
    # TODO: Aquí empieza a escribir tu código de Python para el reporte
    print("Generando datos del reporte...")



# --- MENÚ PRINCIPAL DEL PROYECTO ---
def menu():
    while True:
        print("\n--- MENÚ DEL TRABAJO FINAL ---")
        print("1. Ejecutar Parte 1 (Registro)")
        print("2. Ejecutar Parte 2 (Gestión)")
        print("3. Ejecutar Parte 3 (Reporte)")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            parte_uno_registro()
        elif opcion == "2":
            parte_dos_gestion()
        elif opcion == "3":
            parte_tres_reporte()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar el menú al iniciar el archivo
if __name__ == "__main__":
    menu()
