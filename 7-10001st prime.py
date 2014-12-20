from math import sqrt

def is_prime(n):
    if n==2:
        return True
        
    for x in xrange(2, int(sqrt(n))+2):
        if n%x == 0:
            return False
    return True
    
current_number = 1
prime_counter = 0

while prime_counter < 10001:
    current_number +=1
    if is_prime(current_number):
        prime_counter +=1
        print prime_counter
    
print current_number