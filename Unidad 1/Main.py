from Model.Clases import *

listaAutos = []
listaMecs = []
listaReparaciones = []


while True:
    Menu.LimpiarConsola()
    Menu.MostrarMenu()

    opcionSeleccionada = input(" : ")

    if (opcionSeleccionada == "7"):
        Menu.LimpiarConsola()
        #Editar Info de un Auto
        print("--------------------Opcion de Modificaion de Auto----------------------------")
        print("Seleccione el Auto que desea Modificar: ")
        print(" ")

        i = 1
        for A in listaAutos:
            print(f"Opcion {i} : {A.getInfo()}")
            i += 1    
        opcion = int(input(" : "))

        pat = input("Ingresa su Patente: ")
        chas = input("Ingresa su Numero de Chasis: ")
        mar = input("Ingresa su Marca: ")
        model = input("Ingresa su Modelo: ")
        col = input("Ingresa su Color: ")
        año = input("Ingresa su Año: ")

        AutoModificado = Auto(pat, chas, mar, model, col, año)

        listaAutos[opcion - 1] = AutoModificado

        input("Auto Modificado Exitosamente! Presione Enter para continuar...")

    if (opcionSeleccionada == "8"):
        Menu.LimpiarConsola()
        #Eliminar Info de un Auto
        print("--------------------Opcion de Eliminacion de Auto----------------------------")
        print("Seleccione el Auto que desea Eliminar: ")
        print(" ")

        i = 1
        for A in listaAutos:
            print(f"Opcion {i} : {A.getInfo()}")
            i += 1    
        opcion = int(input(" : "))
        listaAutos.remove(listaAutos[opcion - 1])
        input("Auto Eliminado Exitosamente! Presione Enter para continuar...")

    if(opcionSeleccionada == "1"):
        Menu.LimpiarConsola()
        #Logica para Agregar Autos a la Base de Datos
        print("--------------------Opcion de Ingreso de Autos----------------------------")
        pat = input("Ingresa su Patente: ")
        chas = input("Ingresa su Numero de Chasis: ")
        mar = input("Ingresa su Marca: ")
        model = input("Ingresa su Modelo: ")
        col = input("Ingresa su Color: ")
        año = input("Ingresa su Año: ")

        A = Auto(pat, chas, mar, model, col, año)

        listaAutos.append(A)
        input("Auto Ingresado Exitosamente! Presione Enter para continuar...")

    if(opcionSeleccionada == "2"):
        print("--------------------Opcion de Ingreso de Mecanicos----------------------------")
        rut = input("Ingresa su Rut: ")
        nom = input("Ingresa su Nombres: ")
        ape = input("Ingresa su Apellidos: ")
        correo = input("Ingresa su Correo: ")

        M = Mecanico(rut,nom,ape,correo)

        listaMecs.append(M)
        input("Mecanico Ingresado Exitosamente! Presione Enter para continuar...")


    if (opcionSeleccionada == "3"):

        Menu.LimpiarConsola()
        print("--------------------Opcion de Ingreso de Reparacion----------------------------")

        #len(listaAutos) # 1,2,3,4
        #len(listaMecs) # 1,2,3,4

        if( (len(listaMecs) > 0) & (len(listaAutos) > 0)): 
            print("Selecciona de la Siguiente Lista un Mecanico para que realice la Reparacion: ")
            print(" ")
            i = 1
            for M in listaMecs:
                print(f"Opcion {i} : {M.getInfo()}")
                i += 1   
            opcion = int(input(" : "))
            mecSeleccionado = listaMecs[opcion - 1]
            i = 1
            for A in listaAutos:
                print(f"Opcion {i} : {A.getInfo()}")
                i += 1    
            opcion = int(input(" : "))
            autoSeleccionado = listaAutos[opcion - 1]
            valor = input("Valor de la Reparacion?: ")
            repuesto = input("Ingrese Repuesto Utilizado: ")
            Rep = Reparacion(autoSeleccionado, mecSeleccionado, valor, repuesto)
            listaReparaciones.append(Rep)
            print("Reparacion Ingresada Correctamente!")
        else:
            print("Debes Ingresar Autos/Mecanicos para poder crear una Reparacion!")
        print(" ")
        input("Presione Enter para Continuar...")



    if(opcionSeleccionada == "4"):
        #Mostrar el Listado de Vehiculos del Sistema
        Menu.LimpiarConsola()
        print("--------------------Opcion de Ver Autos----------------------------")
        for A in listaAutos:
            print(A.getInfo()) 
        input("Presione Enter para continuar...")

    if(opcionSeleccionada == "5"):
        #Mostrar el Listado de Vehiculos del Sistema
        Menu.LimpiarConsola()
        print("--------------------Opcion de Ver Mecanicos----------------------------")
        for M in listaMecs:
            print(M.getInfo()) 
        input("Presione Enter para continuar...")

    if(opcionSeleccionada == "6"):
        #Mostrar el Listado de Reparaciones del Sistema
        Menu.LimpiarConsola()
        print("--------------------Opcion de Ver Reparaciones----------------------------")
        for R in listaReparaciones:
            print(R.getInfo()) 
        input("Presione Enter para continuar...")


    



    if(opcionSeleccionada == "0"):
        break