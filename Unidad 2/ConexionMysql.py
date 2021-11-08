import mysql.connector
from Model.Clases import *
from mysql.connector import errorcode
class DAO:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user='root', password='',
                host='127.0.0.1',
                database='test2')

            print('Conexion MySql Establecida Correctamente!')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)


    def InsertarCliente(self, C):
        
        add_cliente = ("INSERT INTO tbl_clientes"
                    "(rut, nombres, apellidos, correo, telefono, direccion, comuna)"
                    "VALUES"
                    "(%s, %s, %s, %s, %s, %s, %s)")
        data_cliente = (C.getRut(),C.getNombres(),C.getApellidos(),C.getCorreo(),C.getTelefono(),C.getDireccion(),C.getComuna())   
        
        cursor = self.cnx.cursor()
        cursor.execute(add_cliente, data_cliente)
        self.cnx.commit()