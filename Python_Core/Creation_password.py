#Creación de contraseña repitiendo el campo:
password = input()
repeat = input()

def validate(text1, text2):
    if text1 == text2: #Validacion de dos campos que deben ser iguales.
        print("Correct")
    else:
        print("Wrong")


validate(password, repeat)