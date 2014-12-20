def number_of_divisors(number):
    divisors = dict()
    while number != 1:
        possible_divisor = 2
        while True:
            if number % possible_divisor == 0:
                divisors_qty = divisors.get(possible_divisor, 0)
                divisors[possible_divisor] = 1 + divisors_qty
                number = number / possible_divisor
                break
            possible_divisor +=1
    total_of_divisors = 1
    for k,v in divisors.items():
        total_of_divisors *= (v+1)
    return total_of_divisors
   
total = 0
n = 1
while True:
    total += n
    if number_of_divisors(total) > 500:
        print total
        break
    n+=1

