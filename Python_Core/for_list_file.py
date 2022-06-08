#RECUPERAR COMO LISTA CONTENIDO DE UN ARCHIVO POR MEDIO DE FOR()
file = open("test.txt", "r")
for i in file:
  print(i)
file.close()