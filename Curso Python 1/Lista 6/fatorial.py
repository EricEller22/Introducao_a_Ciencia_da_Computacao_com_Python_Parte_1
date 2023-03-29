
n = int(input("Digite um número da sequência ou 0 para encerrar:"))
while n != 0:
    fat = 1
    while n > 1:
        fat =  fat * n
        n -= 1
    print(fat)
    n = int(input("Digite um número da sequência ou 0 para encerrar:"))
    
print("Sequência encerrada!")   
    
