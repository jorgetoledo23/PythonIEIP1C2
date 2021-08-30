from Test import Auto

miAuto = Auto()  #Objeto => Instanciacion

miAuto.año = 2013
miAuto.color = "Blanco"
miAuto.marca = "Kia"
miAuto.numeroChasis = "KNZ2304655727636"
miAuto.patente = "FSTR45"
miAuto.tipoCombustible = "Gasolina"

print(miAuto.color)
print(miAuto.marca)
print(miAuto.tipoCombustible)
#print(miAuto.estado)
#miAuto.Encender()
#print(miAuto.estado)

otroAuto = Auto()
otroAuto.Encender()
print("El Estado de OtroAuto es: ", otroAuto.estado)
print("El Estado de miAuto es: ", miAuto.estado)