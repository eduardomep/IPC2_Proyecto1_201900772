def print_menu():
    print("""
------- FIUSAC - Generador de reportes --------
|                                             |
|  1. Cargar archivo                          |
|  2. Procesar archivo                        |
|  3. Escribir archivi de salida              |
|  4. Mostrar datos del estudiante            |
|  5. Generar gráfica                         |
|  6. Salir                                   |
|                                             |
-----------------------------------------------""")
    menu_selector()

#import upload_file

def menu_selector():
    print("Seleccione una opcion para continuar:")
    menu_option = str(input())
    if(menu_option == "1"):
        #upload_file.get_file()
        print(f"Seleccionaste {menu_option}")

    elif(menu_option == "2"):
        print(f"Seleccionaste {menu_option}")
    elif(menu_option == "3"):
        print(f"Seleccionaste {menu_option}")
    elif(menu_option == "4"):
        print(f"Seleccionaste {menu_option}")
    elif(menu_option == "5"):
        exit
    else:
        print(f"{menu_option} no es un opción válida, intenta de nuevo \n")
        menu_selector()
    