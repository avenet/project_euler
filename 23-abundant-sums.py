import math 
  
abundant_numbers = set()
not_expressable_sum = 0
  
def sum_of_proper_divisors(n):
    proper_sum = 1
    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
            if x**2 != n:
                proper_sum += (x + n/x)
            else:
                proper_sum += x
    return proper_sum

is_abundant = lambda n :  sum_of_proper_divisors(n) > n   

for number in xrange(28124):
    expressable = False
    for abundant in abundant_numbers:
        if (number - abundant) in abundant_numbers:
            expressable = True
            break
    
    if not expressable:
        not_expressable_sum += number

    if is_abundant(number):
        abundant_numbers.add(number)

print not_expressable_sum