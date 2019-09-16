#Rosalind | Fibonacci Numbers

def fibo(n):
    if n == 0:
        pout = 0
    elif n == 1:
        pout = 1
    else:
        counter = 2
        pinit = 1
        trans = 1
        while counter < n:
            pout = pinit + trans
            pinit = trans
            trans = pout
            counter += 1
    return pout
        
print(fibo(24))