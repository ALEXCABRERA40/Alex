#Creamos un archivo con notas personales
with open("my_notes.txt.","w") as nota:
    nota.write("Recuerda la fecha de los examenes.\n")
    nota.write("Recuerda que tengo partido a las 7pm.\n")
    nota.write("recuerda tomar tus pastillas.\n")

print("¡notas escritas!")

#abrimos el archico
with open("my_notes.txt.","r") as nota:
    print("contenido del archivo:")

#leemos el archivo linea por linea
    for linea in nota:
        print(linea)
        linea = linea.strip()
        print(linea)








