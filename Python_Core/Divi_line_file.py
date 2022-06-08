#Ciclo para recorrer el archivo e imprimir de a 4 caracteres en cada linea:
file = open("filename.txt", "r")
for i in range(21):
  print(file.read(4))
file.close()