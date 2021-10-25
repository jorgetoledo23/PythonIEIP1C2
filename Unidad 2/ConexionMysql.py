import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='d_iei_n2_p1_c2')


print('Conexion a Mysql Establecida')

cnx.close()