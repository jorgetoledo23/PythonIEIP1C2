from Clases import Auto, Reparacion, Mecanico

autoFordFiesta = Auto("FSXG54", "67236732463742FGASFGFG")
print(autoFordFiesta.getPatente()) # => FSXG54

mecanicoJuan = Mecanico("17.534.281-K", "Juan Enrique","Fernandez Toledo", "Merced 503, Curico", "mecanicoJuan@gmail.com")
print(mecanicoJuan.getInfoMecanico())
#17.534.281-K Juan Enrique Fernandez Toledo Merced 503, Curico mecanicoJuan@gmail.com

mecanicoJuan.uptDireccion("Yungai 375, Curico")
print(mecanicoJuan.getInfoMecanico())

#17.534.281-K Juan Enrique Fernandez Toledo Merced 503, Curico mecanicoJuan@gmail.com
#17.534.281-K Juan Enrique Fernandez Toledo Yungai 375, Curico mecanicoJuan@gmail.com




reparacionFordFiesta = Reparacion("17.172.234-0", "18.290.343-K")
reparacionFordFiesta.autoReparado = autoFordFiesta
reparacionFordFiesta.autoReparado.patente = "ZZZG45"

#print(reparacionFordFiesta.autoReparado)
