import os

class Auto:
    
    def __init__(self, pat, nchas, marca, modelo, color, año):
        self.__Patente = pat
        self.__NChasis = nchas
        self.__Marca = marca
        self.__Modelo = modelo
        self.__Color = color
        self.__Año = año

    def getInfo(self):
        return f"Auto Patente: {self.__Patente}, Marca: {self.__Marca}, Modelo: {self.__Modelo}, Color: {self.__Color}, Año: {self.__Año}"
        #return "Auto Patente: " + self.__Patente + ", Marca: " + self.__Marca

class Mecanico:
    
    def __init__(self, rut, nom, ape, correo):
        self.__Rut = rut
        self.__Nombres = nom
        self.__Apellidos = ape
        self.__Correo = correo

    def getInfo(self):
        return f"Mecanico Rut: {self.__Rut}, Nombre: {self.__Nombres}, Apellido: {self.__Apellidos}, Correo: {self.__Correo}"

class Reparacion:
    pass

class Menu:

    def MostrarMenu():

        print("-----------------------------SISTEMA DE REPARACIONES-------------------------")

        print("Presione 1 para Agregar Auto: ")
        print("Presione 2 para Agregar Mecanico: ")
        print("Presione 3 para Agregar Reparacion: ")

        print("Presione 4 para Ver Autos Ingresados: ")
        print("Presione 5 para Ver Mecanicos Ingresados: ")
        print("Presione 6 para Ver Reparaciones Ingresados: ")

        print("Presione 0 y Enter para Salir!")

    def LimpiarConsola():
        if(os.name == "nt"):os.system("cls")
        else: os.system("clear")
            
    def OpcionSeleccionada():
        pass

