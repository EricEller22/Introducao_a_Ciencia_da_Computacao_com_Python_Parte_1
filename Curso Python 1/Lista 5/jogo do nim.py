
print("Bem-vindo ao jogo no NIM! Escolha:")

def inicio():
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    

    n = 0
    while n >= 0 and n < 2:
        n = int(input(""))
        if n == 1:
            print("Você escolheu uma partida isolada!")
            return 1
        if n == 2:
            print("Voce escolheu um campeonato!")
            return 2
        if n != 1 and n != 2:
            print("Tente novamente!")
            return inicio()

def computador_escolhe_jogada(n, m):
    prox_jogada =  n  % (m + 1)
    if prox_jogada == 0:
        prox_jogada = m
    return prox_jogada
    
 
def  usuario_escolhe_jogada(n, m):
    jogada = int(input("Informe a sua jogada: "))
    while jogada > m or jogada > n or jogada < 1:
        print("Informe uma jogada válida")
        jogada = int(input("Informe quantas peças você vai retirar:"))
    return jogada


def partida(n,m):

    if n % (m + 1) == 0:
        print("Você começa!")
        jogador = True
    else:
        print("Computador começa!")
        jogador = False
    while n > 0:
        if  jogador == True:
            x = usuario_escolhe_jogada(n, m)
            n -= x
            print("Você tirou", x, "peças")
            jogador = False
        else:
            x = computador_escolhe_jogada(n, m)
            n -= x
            print("O compuador tirou", x, "peças")
            jogador = True
        print("Restaram apenas", n, "peças no tabuleiro")
    if jogador == True:
        print("O computador venceu!!!")
    else:
        print("Você venceu!")


def partida_isolada():
    print("Você vai jogar uma partida isolada!")
    n = int(input("Informe a quantidade de peças:"))
    m = int(input("Informe o limite de peças por jogada:"))
    print(partida(n,m))

def campeonato():
    print("Você irá jogar um campeonato!!!")
    
    x = 0
    while x <= 3:
        n = int(input("Informe a quantidade de peças:"))
        m = int(input("Informe o limite de peças por jogada:"))
        print(" Rodada %d "%x)
        print(partida(n,m))
        x += 1
        

    print(" Final do campeonato! ")
    print(" Placar: Você 0 X 3 Computador")

    
if inicio() == 1:
    print(partida_isolada())
if inicio() == 2:
    print(campeonato())


