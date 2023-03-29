def maior_primo(x):
    
    primo = False
    
    if x < 0:
        x = 2
        return(x)
    if x % 2 == 1:
            return(x)
        
    while primo != True:
        c = x % 2
        x2 = x
        x = x - 1
        if ((((c >= 1) and (x2 % 2 >= 1)) and (x2 % 3 >= 1)) and ((x2 % 5 >= 1) and (x2 % 7 >= 1))) == True :
            primo = True
            return(x2)
        else:
            primo = False

     
        
        
    
        
    
