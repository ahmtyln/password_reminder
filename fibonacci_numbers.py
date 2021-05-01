flist=[]
def fibonacci_numbers():
    x=1
    flist.append(x)
    flist.append(x)
    i=1
    while flist[i]<55:
        flist.append(flist[i]+flist[i-1])
        i+=1
   
fibonacci_numbers()
print(flist)

