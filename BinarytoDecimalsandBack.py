
def changetobinary(n):
    binarylist = []
    while n//2 !=0:
        rem = n%2
        binarylist.append(rem)
        n = n//2
    
    rem = n%2
    binarylist.append(rem)
    
    
    return int("".join(map(str, binarylist[::-1])))

def changetodecimals(n):
    n = [int(i) for i in str(n)]
    length = len(n)
    result = 0
    for i in n:
        length -=1
        result += i*(2**(length))
        
    return result