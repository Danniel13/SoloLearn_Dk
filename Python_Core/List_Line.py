#CREAR LINEAS DE UN ARCHIVO CREADO A PARTIR DE UNA LISTA
names = ["John", "Oscar", "Jacob"]

file = open("names.txt", "w+")
#write down the names into the file
# print(names[0],"\n",names[1],"\n",names[2])
for i in names:
  file.write(i+"\n")


# print(names[1])
# print(names[2])
file.close()

file= open("names.txt", "r")
#output the content of file in console
print(file.read())

file.close()

file2= open("prueba.txt", "w")

msg="los patos vuelan"

print(file2.write(msg) == len(msg))
print(file2.write(msg) == msg)