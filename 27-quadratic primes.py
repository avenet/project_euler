from math import sqrt

evaluate = lambda a,b,n : n**2 + a*n + b

max_primes, max_a, max_b = (0, 0, 0)

def is_prime(n):
    if n < 0:
        n = -1*n
    elif n == 0 or n == 1:
        return False
    
    if n==2: 
        return True
          
    for x in xrange(2, int(sqrt(n))+2): 
        if n%x == 0: 
            return False
    return True

def count_primes(a, b):
    n = 0
    while is_prime(evaluate(a,b,n)):
        n += 1
    return n

for a in xrange(-1000, 1000):
    for b in xrange(-1000, 1000):
        primes_quantity = count_primes(a,b)
        if primes_quantity > max_primes:
            max_primes, max_a, max_b = primes_quantity, a, b
            
print count_primes(-79,1601)
print max_a * max_b