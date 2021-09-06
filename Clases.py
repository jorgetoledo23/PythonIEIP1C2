class Auto:
    #Atributos => Caracteristicas
    color = "" 
    tipoCombustible = "" #Diesel / Gasolina / Electrico
    marca = ""
    numeroChasis = ""
    estado = False #Boolean
    año = 0

    #Constructor // Se ejecuta por defecto al instanciar esta clase
    def __init__(self, pat, nchas):
        self.__patente = pat
        self.numeroChasis = nchas

    #Metodos
    def encender(self):
        self.estado = True

    def getEstado(self):
        return self.estado

    def getPatente(self):
        return self.__patente
    


class Reparacion:
    codigoReparacion = ""
    reparacionesRealizadas = []
    repuestosUtilizados = []
    rutCliente = ""
    rutMecanico = ""
    Valor = 0
    autoReparado = None #Auto Reparado

    def __init__(self, rutC, rMec):
        self.rutCliente = rutC
        self.rutMecanico = rMec


class Mecanico:
    def __init__(self, rut, nom, ape, dir, email):
        self.__RUT = rut
        self.__nombres = nom
        self.__apellidos = ape
        self.__direccion = dir
        self.__correoElectronico = email

    # Concepto de Encapsulacion
    def getInfoMecanico(self):
        return self.__RUT + " " + self.__nombres + " " + self.__apellidos + " " + self.__direccion + " " + self.__correoElectronico

    def uptDireccion(self, value):
        self.__direccion = value

    def getRutMecanico(self):
        return self.__RUT


class Animal:
    #Atributos => Caracteristicas
    DNI = ""
    nombreComun = ""
    nombreCientifico = ""

class Vendedor:

    #Atributos => Caracteristicas
    RUT = ""
    nombre = ""
    apellidos = ""
    direccion = ""
    correoElectronico = ""