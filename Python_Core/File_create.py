# open("test.txt", "w")  # File Creation
# file = open("test.txt") #Variable creation
# cont = file.read()  #variable read creation
# print(cont) #Print File
# file.close() #Close File


file = open("test.txt", "r")
for i in range(21):
  print(file.read(4))
file.close()
