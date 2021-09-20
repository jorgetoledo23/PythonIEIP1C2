from Model.Clases import *

listaAutos = []
listaMecs = []
listaReparaciones = []


while True:
    Menu.LimpiarConsola()
    Menu.MostrarMenu()

    opcionSeleccionada = input(" : ")

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


    if(opcionSeleccionada == "0"):
        break