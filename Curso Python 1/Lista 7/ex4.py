
cont = 1
lista = []

while cont > 0:
    n = int(input("Digite um número: "))
    lista.append(n)
    cont = n

cont3 = -1
cont2 = len(lista)

for elementos in lista:  
    if cont2 >= 2:
        cont3 = cont3 - 1
        print(lista[cont3])
    cont2 -= 1
