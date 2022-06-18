#Programa para evaluar un texto introducido: Evalua la cantidad de veces que esta una letra que se le pide al usuario y el porcentaje de 
#cada una de las letras del abecedario en el mismo texto

def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

Text1=input("Introduzca el texto a evaluar: ")
val1= input("Introduzca la letra o vocal a evaluar dentro del texto: ")


print("La cantidad de veces que esta la letra","'", val1, "' es: ", count_char(Text1, val1))

print("El porcentaje por caracter evaluado en el texto ingresado es el siguiente:","\n")

for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(Text1, char) / len(Text1)
  print("{0} - {1}%".format(char, round(perc, 2)))