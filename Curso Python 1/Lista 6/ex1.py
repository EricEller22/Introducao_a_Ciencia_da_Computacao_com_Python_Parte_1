largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

while altura > 0:
    x = largura
    while largura > 1:
        print("#", end = "")
        largura -= 1
    largura = x    
    print("#")
    altura -= 1
    
