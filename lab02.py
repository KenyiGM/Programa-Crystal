import os

def programa():

    print("\n\n    Iniciando programa....\n")

    print("""

        ┌•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•┐
        ║                                               ║
        ║                Programa Crystal               ║
        ║                                               ║
        └•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•┘

                ♥ ♦ ♣ ♠ Bienvenidos ♠ ♣ ♦ ♥

    """)

    nom = input("   Como deseas llamarte: ")

    while True:

        print(f"""

        ► Hola {nom}

        (Esta aplicación solo fue probado en Windows)

        Estas son las herramientas que puede hacer el programa

        1. Creacion de carpetas de trabajo en cmd
        2. Ordenar archivos en cmd
        3. Buscar archivos en cmd
        4. Eliminar archivos y carpetas en cmd
        5. Limpiar el cmd
        6. Salir

        """)
        try:
            opcion = int(input("    (Solo se permiten numeros)\n\n    ► "))

            os.system("cls")
            
            match opcion:
                
                case 1:
                    try:
                        nro_carpeta = int(input("\n   ¿Cuantas carpetas deseas crear?\n\n    ► "))
                        for num in range(1,nro_carpeta+1):
                            nom_carpeta = input("\n   ¿Que nombre quieres ponerle?\n\n    ► ")
                            os.system(f"    md {nom_carpeta}")
                    except:
                        print("Algo salio mal, vuelva a intentarlo")
                case 2:
                    os.system("cls")
                    print("""
                    
            ¿Como deseas ordenar las carpetas?

            1.- N  Por nombre (orden alfabético)
            2.- E  Por extensión (orden alfabético)
            3.- S  Por tamaño (orden creciente)
            4.- D  Por fecha y hora (el más antiguo primero)

            5.- Volver al menu
                    
                    """)
                    try:
                        opcion_archivos = int(input("   (Solo se permiten numeros)\n\n     ► "))
                        print("\n")
                        match(opcion_archivos):
                            case 1:
                                os.system("cls")
                                os.system("    dir /ON")
                                input("\npresiona enter para continuar...")
                                os.system("cls")
                            case 2:
                                os.system("cls")
                                os.system("    dir /OE")
                                input("\npresiona enter para continuar...")
                                os.system("cls")
                            case 3:
                                os.system("cls")
                                os.system("    dir /OS")
                                input("\npresiona enter para continuar...")
                                os.system("cls")
                            case 4:
                                os.system("cls")
                                os.system("    dir /OD")
                                input("\npresiona enter para continuar...")
                                os.system("cls")
                            case 5:
                                pass
                    except:
                        print("Algo salio mal, vuelva a intentarlo")
                case 3:     
                    print("\n Escribe el nombre del archivo que deseas buscar ..")
                    ar_b = input("\n\n ► ")
                    os.system(f"cd *:/ & dir {ar_b}.* /s")
                    input("\npresiona enter para continuar...")
                    os.system("cls")
                case 4:

                    os.system("dir") 
                    print("\n ¿Deseas eliminar carpeta o archivo?")
                    try:
                        ar_o_car = input("\n\n ► ")
                        while True:
                            match(ar_o_car):
                                case "carpeta":
                                    nombre_car = input("\n Escriba el nombre de la carpeta : \n\n ► ")
                                    os.system(f"rd /S {nombre_car}")
                                    False
                                    break
                                case "archivo":
                                    nombre_ar = input("\n Escribe el nombre del archivo.extension : \n\n ► ")
                                    os.system(f"del /f /a {nombre_ar}")
                                    False
                                    break
                                case _:
                                    print("Vuelva a escoger de nuevo")    
                        input("\n presiona enter para continuar...")
                        os.system("cls")
                    except:
                        print("\n No se pudo efectuar la operación")
                case 5:
                    os.system("cls")
                case 6:
                    print("""

                    PROGRAMA CRYSTAL

                ░░░░░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░▄██▄░░░░░▄█▄░░░
                ░░░░░░░░▐███▀▀▀░▀▄███▌░░
                ░░░▄▄▀▀▄█▀▀░░░░░░░░▀██░░
                ░░█░░░██░░░░░░░░░░░░░▀▄░
                ░█▌░░▐██░░ ██░░░██ ░░░█░
                ░██░░▐██▄░ █▀░░░▀█ ░░▐▌░
                ░██▄░▐███▄░░░▄▄▄░░░░▄██░
                ░▐███▄██████▄░▀░▄█████▌░
                ░▐████████████▀▀██████░░
                ░░▐████▀██████░░█████░░░
                ░░░░▀▀▀░░█████▌░████▀░░░
                ░░░░░░░░░░▀▀███░▀▀▀░░░░░
                ░░░░░░░░░░░░░░░░░░░░░░░░

                    (Kenyi Galindo)

        ¡¡¡ Muchas Gracias por usar el programa  !!!               
                    
                    """)
                    break
                case _:
                    print("\n       No se encontro nada")
        except:
            print("Algo salio mal, vuelva a intentarlo")

if __name__ == "__main__":
    programa()