import math

sum_of_divisors_map = {}
amicable_numbers = []

def sum_of_divisors(n):
    return 1 + sum([x+n/x for x in range(2, int(math.sqrt(n)) + 1) if n%x==0])
    
for x in range(1, 10000):
    divisors_sum = sum_of_divisors(x)
    if x > divisors_sum and sum_of_divisors_map.get(divisors_sum, -1) == x:
        amicable_numbers.append(divisors_sum)
        amicable_numbers.append(x)
    sum_of_divisors_map[x] = divisors_sum