import collections

def factor_descomposition(number):
    while number != 1:
        possible_divisor = 2
        while True:
            if number % possible_divisor == 0:
                yield possible_divisor
                number = number / possible_divisor
                break
            possible_divisor +=1
            
            
def smallest_multiple(n):
    prime_factors = dict()
    for number in range(2, n+1):
        item_counter = dict(collections.Counter([x for x in factor_descomposition(number)]))
        for item,count in item_counter.items():
            if prime_factors.get(item, 0) < count:
                prime_factors[item] = count
            
    result_list = [x**y for x,y in prime_factors.items()]
    return reduce(lambda x,y: x*y, result_list)
    
print smallest_multiple(20)