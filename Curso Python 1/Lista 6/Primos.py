
n = int(input("Digite um número inteiro: "))

def primo(n):
    fator = 2
    while n % fator != 0 and fator <= n/2:
        fator += 1
    if n % fator == 0:
        return False
    else:
        return True
        

while n > 0:
    if primo(n):
        print(n,"é primo!")
    else:
        print(n,"não é primo!")
    n = int(input("Digite um número inteiro: "))


    
