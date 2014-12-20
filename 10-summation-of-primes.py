from math import sqrt
def is_prime(n):
    if n==2:
        return True
        
    for x in xrange(2, int(sqrt(n))+1):
        if n%x == 0:
            return False
    return True
    
upper_bound = 2*10**6
n = 3
full_sum = 2

while n < upper_bound:
    if is_prime(n):
        full_sum += n
    n+=2
    
print full_sum