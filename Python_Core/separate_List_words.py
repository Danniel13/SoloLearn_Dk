#Separar texto de entrada en una lista de palabtas que lo componen


txt = input()

def words(var):
    #your code goes here
    for i in var.split():
      yield i

print(list(words(txt)))