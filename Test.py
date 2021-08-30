class Auto:
    #Atributos => Caracteristicas
    color = "" 
    tipoCombustible = "" #Diesel / Gasolina / Electrico
    marca = ""
    patente = ""
    numeroChasis = ""
    estado = False #Boolean
    año = 0

    #Metodos
    def Encender(self):
        self.estado = True

    def GetEstado(self):
        return self.estado

class Reparacion:
    codigoReparacion = ""
    reparacionesRealizadas = []
    repuestosUtilizados = []
    rutCliente = ""
    rutMecanico = ""
    VehiculoReparado = ""
    Valor = 0

class Animal:
    #Atributos => Caracteristicas
    DNI = ""
    nombreComun = ""
    nombreCientifico = ""

class Vendedor:
    #Atributos => Caracteristicas
    DNI = ""
    nombre = ""
    apellidos = ""
    direccion = ""
    correoElectronico = ""
