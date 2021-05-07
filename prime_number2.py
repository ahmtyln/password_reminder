def prime_number(n):
    liste=[]
    liste1=list(range(2,n))
    
    for i in range(3,n):
        for ii in range(2,i):
            if i%ii == 0:
                liste.append(i)
                break
    k1=set(liste)
    k2=set(liste1) 
        
    return list(k2-k1)
print(prime_number(100))