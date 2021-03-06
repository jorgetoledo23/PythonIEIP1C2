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

            for C in dao.ListarClientes():
                print(C.getInfoDetallada())

            print("")
            oP = None
            input('Presione Enter para Continuar...')    

        if oP == "3":
            #Editar/Actulizar algun cliente
            mP.LimpiarConsola()
            print("======= Editando Clientes =======")
            print("=================================")
            print("======= Seleccione el Cliente que desea Actualizar =======")
            print("")

            for C in dao.ListarClientes():
                print(C.getInfoDetallada())

            RutAntiguo = input("Digite Rut del Cliente: ")

            mP.LimpiarConsola()
            print(f"======= Editando Cliente: {RutAntiguo} =======")
            print("============== Complete la Informacion ===================")
            print("")

            Rut = str(input("Rut: "))
            Nombres = str(input("Nombres: "))
            Apellidos = str(input("Apellidos: "))
            Telefono = str(input("Telefono: "))
            Correo = str(input("Correo: "))
            Direccion = str(input("Direccion: "))
            Comuna = str(input("Comuna: "))
            C = Cliente(Rut,Nombres,Apellidos,Correo,Telefono,Direccion,Comuna)

            dao.ActualizarCliente(C, RutAntiguo)
            mP.ConfirmacionEdit('Cliente')


        if oP == "4":
            #Eliminar un cliente en especifico
            mP.LimpiarConsola()
            print("======= Eliminando Cliente =======")
            print("=================================")
            print("======= Seleccione el Cliente que desea Eliminar =======")
            print("Tener cuidado ya que no se puede recuperar la informacion")
            print("")

            for C in dao.ListarClientes():
                print(C.getInfoDetallada())

            Rut = input("Digite Rut del Cliente: ")

            confirmacion = input(f"Estas seguro de que quieres eliminar el cliente: {Rut} ? (Y/N)")
            if confirmacion == "Y":
                dao.EliminarCliente(Rut)
                mP.ConfirmacionDelete('Cliente')
            if confirmacion == "N":
                pass


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

            for M in dao.ListarMecanicos():
                print(M.getInfoDetallada())

            print("")
            input('Presione Enter para Continuar...')

        if oP == "3":
            #Editar/Actulizar algun Mecanico
            mP.LimpiarConsola()
            print("======= Editando Mecanicos =======")
            print("=================================")
            print("======= Seleccione el Mecanico que desea Actualizar =======")
            print("")

            for M in dao.ListarMecanicos():
                print(M.getInfoDetallada())

            RutAntiguo = input("Digite Rut del Mecanico: ")

            mP.LimpiarConsola()
            print(f"======= Editando Mecanico: {RutAntiguo} =======")
            print("============== Complete la Informacion ===================")
            print("")

            Rut = str(input("Rut: "))
            Nombres = str(input("Nombres: "))
            Apellidos = str(input("Apellidos: "))
            Telefono = str(input("Telefono: "))
            Correo = str(input("Correo: "))
            Direccion = str(input("Direccion: "))
            Comuna = str(input("Comuna: "))
            M = Mecanico(Rut,Nombres,Apellidos,Correo,Telefono,Direccion,Comuna)

            dao.ActualizarMecanico(M, RutAntiguo)
            mP.ConfirmacionEdit('Mecanico')

        if oP == "5":
            pass

    if oP == "3":
        #Gestionamos Vehiculos
        mP.LimpiarConsola()
        mP.MenuGestion("Vehiculo")
        oP = str(input(" : "))

        if oP == "1":
            #Ingresar nuevo Vehiculo
            mP.LimpiarConsola()
            print("======= Agregando Vehiculo =======")
            print("Complete la Informacion Solicitada:")
            print("")

            Patente = input("Ingrese Patente: ")
            Marca = input("Ingrese Marca: ")
            Modelo = input("Ingrese Modelo: ")
            Year = input("Ingrese Year: ")
            NChasis =  input("Ingrese Numero de Chasis: ")
            Color = input("Ingrese Color: ")

            mP.LimpiarConsola()
            print("======= Seleccion Cliente =======")
            print("")

            for C in dao.ListarClientes():
                print(C.getInfo())

            print("")
        
            rutCliente = input("Ahora Ingrese Rut del Cliente de la Lista Anterior: ")

            A = Auto(Patente, NChasis, Color, Marca, Year, Modelo, rutCliente)

            dao.InsertarVehiculo(A)

            mP.ConfirmacionIngreso("Vehiculo")

        if oP == "2":
            #listar Vehiculos
            mP.LimpiarConsola()
            print("======= Listando Vehiculos =======")
            print("=================================")
            print("")

            for A in dao.Listar('Vehiculo'):
                print(A.getInfo())

            print("")
            input("Presione Enter para Continuar...")
