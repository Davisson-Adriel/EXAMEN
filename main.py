from utilidades import*
from archivos import*

cargar_arch("general.json")
cargar_arch("generos.json")
cargar_arch("paises2.json")

while True:
    try:
        mostrar_menu()
        opc=int(input("Ingrese su elecciòn: "))

        if opc==1:
            ag_artista()
        elif opc==2:
            mostrar()
        elif opc==3:
            print()
        elif opc==4:
            ag_paises()
        elif opc==5:
            ag_generos()
        elif opc==6:
            print("Hasta Luego")
            guardar()
            break
        else:
            print("Opciòn invalida")
    except ValueError:
        print("Opciòn invalida")
        
    
