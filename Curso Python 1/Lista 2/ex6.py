import math

n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
n3 = int(input("Digite o terceiro número:"))
n4 = int(input("Digite o quarto número:"))

d = math.sqrt((n1 - n3) ** 2 + (n2 - n4) ** 2)

if d >= 10:
	print("longe")
else: 
	print("perto")
