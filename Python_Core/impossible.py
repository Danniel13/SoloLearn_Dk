weight=float(input("ingrese altura"))
height= int(input("ingrese su peso"))
resultado= float(weight /(height **2))

if resultado < 18.5:
  print("Underweight")
elif resultado >= 18.5 and resultado < 25:
  print("Normal")
elif resultado >= 25 and resultado  < 30:
  print("Overweight")
elif resultado >= 30:
  print("Obesity")