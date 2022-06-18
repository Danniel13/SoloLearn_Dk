txt = input()
# txt2 = txt.split(' ')


txt2 =  max(txt.split(' '), key=len) #-> Max para saber la palabra mas grande------Split para dividir las palabras en una lista sin espacios, 
#Key=len para contar los caracteres en las palabras y sacar la mas grande con max .
#your code goes here
print(txt2)