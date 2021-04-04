import math

def primefactors(n):
    primefactorslist = []
    
    while n % 2 ==0:
        primefactorslist.append(2)
        n = n/2

    for i in range(3, int(math.sqrt(n))+1,2):
        while n % i==0:
            primefactorslist.append(int(i))
            n = n/i
            
    if n >1:
        primefactorslist.append(int(n))
        
    return primefactorslist

