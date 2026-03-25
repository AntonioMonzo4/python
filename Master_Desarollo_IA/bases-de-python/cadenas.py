rol = "Desarrollador"
print(rol)
empresa = "Bytered"
print(empresa)

mensaje = f"Hola, soy {rol} en {empresa}"
mensaje2 = "Hola, soy {} en {}".format(rol, empresa)
mensaje3 = "Hola, soy %s en %s" % (rol, empresa)
mensaje4 = "Hola, soy " + rol + " en " + empresa    
mensaje5 = f"Hola, estos mensajes son iguales: {mensaje == mensaje2 == mensaje3 == mensaje4}"

print(mensaje)
print(mensaje2)
print(mensaje3)
print(mensaje4)