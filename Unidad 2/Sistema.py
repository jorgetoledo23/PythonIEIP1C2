from Model.Clases import *
import ConexionMysql
mP = MenuPrincipal()
dao = ConexionMysql.DAO()
while True:
    mP.LimpiarConsola()
    mP.MostrarMenu()

    oP = str(input(" : "))


    if oP=="1":
        mP.LimpiarConsola()
        mP.MenuClientes()
        oP = str(input(" : "))
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