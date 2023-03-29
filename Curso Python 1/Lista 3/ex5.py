n = int(input("Digite um número inteiro:"))


resto = 1
resto2 = 0
while n == 0:
    print(resto, resto2)
    resto = n % 10
    n = n // 10
    resto2 = n % 10

if resto2 == resto:
    print("sim")
if resto != resto:
    print("não")