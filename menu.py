import upload_file
import graph
import student

def print_menu():
    print("""
------- FIUSAC - Generador de reportes --------
|                                             |
|  1. Cargar archivo                          |
|  2. Procesar archivo                        |
|  3. Escribir archivo de salida              |
|  4. Mostrar datos del estudiante            |
|  5. Generar gráfica                         |
|  6. Salir                                   |
|                                             |
-----------------------------------------------""")
    menu_selector()

def menu_selector():
    print("Seleccione una opcion para continuar:")
    menu_option = str(input())
    if(menu_option == "1"):
        print(upload_file.get_file())
        print_menu()
    elif(menu_option == "2"):
        print(f"Seleccionaste {menu_option}")
    elif(menu_option == "3"):
        print(f"Seleccionaste {menu_option}")
    elif(menu_option == "4"):
        print(student.print_data())
        print_menu()
    elif(menu_option == "5"):
        graph.print_terrains()
        print_menu()
    elif(menu_option == "6"):
        exit
    else:
        print(f"{menu_option} no es un opción válida, intenta de nuevo \n")
        menu_selector()
    