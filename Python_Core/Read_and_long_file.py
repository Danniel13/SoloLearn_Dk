#Leer archivo y validar longitud del contenido:
file = open ("filename.txt", "r")
fileread  = file.read()
print(len(fileread))
file.close()