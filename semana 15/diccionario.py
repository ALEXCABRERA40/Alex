#Diccionario

#Creamos nuestro diccionario
infomacion_personal={"nombre":"Jenny Silva","edad":"24","ciudad":"loja","profesion":"auxiliar de farmacia"}

#modificar el valor de ciudad
infomacion_personal["ciudad"] = "Quito"
infomacion_personal["profesion"] = "auxiliar de farmacia"

#verificar la clave telefono
if "telefono" not in infomacion_personal:
    infomacion_personal["telefono"] = "095388479"

#eliminar la clave edad del diccionario
del infomacion_personal["edad"]

print(infomacion_personal)


