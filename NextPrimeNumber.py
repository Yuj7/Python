import math



def isprime(n):
    
    if n%2 ==0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i ==0:
            return False
        
    return True

def nextPrime(currentPrime):
    
    nextP = currentPrime +1
    
    while True:
        if not isprime(nextP):
            nextP +=1
        else:
            break
    
    return nextP
    

def main():

    currentPrime =2
    while True:
        ans = str(input("Do you want the next prime number? Yes or No: "))

        if ans.lower() == "yes":
            print(currentPrime)
            currentPrime = nextPrime(currentPrime)
        
        else:
            print("Ok :(")
            break
        
        
main()