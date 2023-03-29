n = int(input("Digite um número inteiro: "))

fator = 2
mult = 0

while n > 1:
    while n % fator == 0:
        mult += 1
        n = n / fator
    if mult > 0: 
        print("fator", fator, "multiplicidade = ", mult)
    fator += 1
    mult = 0
