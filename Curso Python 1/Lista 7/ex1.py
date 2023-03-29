def remove_repetidos(lista):
    
    sem_rep = []
    lista.sort()
    
    for numero in lista:
        if numero not in sem_rep:
            sem_rep.append(numero)
    return sem_rep

        
    
    
