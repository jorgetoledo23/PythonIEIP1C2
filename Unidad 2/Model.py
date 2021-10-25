class Auto:
    #Atributos => Caracteristicas
    #Constructor // Se ejecuta por defecto al instanciar esta clase
    def __init__(self, pat, nchas, col, mod, mar, year):
        self.__patente = pat
        self.__numeroChasis = nchas
        self.__color = col,
        self.__año = year
        self.__marca = mar,
        self.__modelo = mod
    #Metodos
    def getInfo(self):
        return f"INFO AUTO: Patente: {self.__patente} "