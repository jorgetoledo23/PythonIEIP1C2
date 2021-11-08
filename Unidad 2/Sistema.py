from Model.Clases import *
from ConexionMysql import DAO
mP = MenuPrincipal()
dao = DAO()
while True:
    mP.LimpiarConsola()
    mP.MostrarMenu()

    oP = str(input(" : "))


    if oP=="1":
        mP.LimpiarConsola()
        mP.MenuGestion("Cliente")
        oP = str(input(" : "))

        #Insertar Cliente en la Base de Datos
        if oP == "1":
            mP.LimpiarConsola()
            print("======= Agregando Cliente =======")
            print("Complete la Informacion Solicitada:")
            print("")

            Rut = str(input("Rut: "))
            Nombres = str(input("Nombres: "))
            Apellidos = str(input("Apellidos: "))
            Telefono = str(input("Telefono: "))
            Correo = str(input("Correo: "))
            Direccion = str(input("Direccion: "))
            Comuna = str(input("Comuna: "))
            C = Cliente(Rut,Nombres,Apellidos,Correo,Telefono,Direccion,Comuna)
            dao.InsertarCliente(C)
            mP.ConfirmacionIngreso('Cliente')

        #Leer desde la Base de Datos TODOS los clientes y mostrarlos
        if oP == "2":
            mP.LimpiarConsola()
            print("======= Listando Clientes =======")
            print("=================================")
            print("")

            for C in dao.LeerClientes():
                print(C.getInfoDetallada())

            print("")
            input('Presione Enter para Continuar...')    

    if oP=="2":
        mP.LimpiarConsola()
        mP.MenuGestion("Mecanico")
        oP = str(input(" : "))

        #Insertar Mecanico en la Base de Datos
        if oP == "1":
            mP.LimpiarConsola()
            print("======= Agregando Mecanico =======")
            print("Complete la Informacion Solicitada:")
            print("")

            Rut = str(input("Rut: "))
            Nombres = str(input("Nombres: "))
            Apellidos = str(input("Apellidos: "))
            Telefono = str(input("Telefono: "))
            Correo = str(input("Correo: "))
            Direccion = str(input("Direccion: "))
            Comuna = str(input("Comuna: "))

            M = Mecanico(Rut,Nombres,Apellidos,Correo,Telefono,Direccion,Comuna)
            dao.InsertarMecanico(M)
            mP.ConfirmacionIngreso('Mecanico')

        #Leer desde la Base de Datos TODOS los Mecanicos y mostrarlos
        if oP == "2":
            mP.LimpiarConsola()
            print("======= Listando Mecanicos =======")
            print("=================================")
            print("")

            for M in dao.LeerMecanicos():
                print(M.getInfoDetallada())

            print("")
            input('Presione Enter para Continuar...')

        if oP == "5":
            pass