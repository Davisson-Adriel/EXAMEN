datos_art={}
paises={}
generos={}

def mostrar_menu():
    print("-----------------------------------------------------------")
    print("1. Registro de artistan\n2. Informes\n3. Reportes\n4. Ingresar Paises\n5. Ingresar Generos\n6. Salir")
    print("-----------------------------------------------------------")

def ag_artista():

    nom=input("Digite el nombre del artista: ")

    while True:
        pai=input("Digite el nombre del pais de origen del artista: ")
        pai=pai.upper()
        eva=paises.get(pai,1)
        if eva==1:
            print("Pais no registrado")
        else:
            break
    
    while True:
    
        yinicio=input("Digite el año de inicio del artista: ")
        if yinicio.isdigit():
            break
        else:
            print("Entrada no valida, intente nuevamente")            

    while True:
    
        yfinal=input("Digite el año de finalizaciòn del artista: ")
        if yfinal.isdigit():
            break
        else:
            print("Entrada no valida, intente nuevamente")       

    yact=(yinicio,"-",yfinal)

    while True:
    
        ydisc=input("Digite el año del primer disco: ")
        if ydisc.isdigit():
            break
        else:
            print("Entrada no valida, intente nuevamente")
    generotemp=[]
    while True:

        gene=input("Ingrese el ID del genero musical: ")
        gene=gene.upper()
        eva=generos.get(gene,1)
        if eva==1:
            print("Genero no registrado")
        else:
            generotemp.append(generos[gene]["Nombre del genero"])
            while True:
                print("¿Desea agregar otro genero?")
                print("1. SI\n2. NO")
                opc=int(input("Ingrese su decisiòn: "))
                if opc==1:
                    print("Genero Adicional")
                elif opc==2:
                    break
        break
    
    ucert=input("Ingrese la cantidad de unidades certificadas: ")
    vent=input("Ingrese las ventas reclamadas: ")
    while True:
        try:
            print("1. ACTIVO\n2. INACTIVO")
            opc=int(input("Ingrese su elecciòn: "))

            if opc==1:
                esta="ACTIVO"
                break
            elif opc==2:
                esta="INACTIVO"
                break
            else:
                print("Opciòn no valida")

        except ValueError:
            print("Ingresos solo numeros enteros")
    
    datos_art[nom]={"Nombre":nom,"Pais de Origen":paises[pai],"Años de actividad":yact,"Año de primer disco":ydisc,"Unidades Certificadas Totales":ucert,"Ventas reclamadas":vent,"Estado del artista":esta,"Generos":generotemp,"Año de inicio":yinicio,"Año final":yfinal}


def ag_paises():
    name=input("Digite el nombre del pais: ")
    name=name.upper()
    cod=input("Digite su codigo ISO: ")
    
    paises[name]= {"Codigo ISO":cod}
    print("Pais registrado con exito")

def ag_generos():
    name=input("Ingrese el nombre del genero musical: ")
    id=input("Ingrese el ID del genero musical: ")

    generos[id]={"Nombre del genero":name}
    print("Genero registrado con exito")

def mostrar():
    temp={}
    temp2={}
    while True:
        pai=input("Digite el nombre del pais de origen del artista: ")
        pai=pai.upper()
        eva=paises.get(pai,1)
        if eva==1:
            print("Pais no registrado")
        else:
            break

    while True:
    
        yinfe=input("Digite el año inferior: ")
        if yinfe.isdigit():
            break
        else:
            print("Entrada no valida, intente nuevamente")
    
    while True:
    
        ysupe=input("Digite el año superior: ")
        if ysupe.isdigit():
            break
        else:
            print("Entrada no valida, intente nuevamente")
    
    for i in datos_art:
        for j in datos_art[i]:
            if j=="Pais de Origen":
                if datos_art[i][j]==pai:
                    temp.append(datos_art[i])

    print(temp)
    for i in temp:
        for j in temp[i]:
            if j=="Año de primer disco":
                if yinfe<=temp[i][j]<=ysupe:
                    temp2.append(temp[i])
    
    for i in temp2:
        print("Arstista --> ", i)
        for j in temp2[i]:
            print(j,"-->",temp2[i][j])
                    



