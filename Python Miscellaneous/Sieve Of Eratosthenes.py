#Sieve Of Eratosthenes
#Program to find all prime numbers
#In the range of 1 to n

def findPrime(n):
    numbers = [True]*(n+1)
    prime = []
    
    k = 2
    while n>=k*k:
        if numbers[k]:
            prime.append(k)
            for num in range(k**2,n+1,k):
                numbers[num] = False        
        k += 1
    
    for p in range(k,n+1):
        if numbers[p]:
            prime.append(p)
                
    print(*prime)


n = int(input())
findPrime(n)
