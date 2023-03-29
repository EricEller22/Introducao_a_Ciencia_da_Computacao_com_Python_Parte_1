def maior_elemento(lista):
    
    maior = 0
    cont = 1
    
    for elemento in lista:
        if elemento < 0 :
            maior = -1
            if elemento < maior:
                maior = elemento
                
        if elemento > maior:
            maior = elemento
            
    return maior
