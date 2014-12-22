from math import sqrt

def factor_descomposition(number):
    while number != 1:
        possible_divisor = 2
        while True:
            if number % possible_divisor == 0:
                yield possible_divisor
                number = number / possible_divisor
                break
            possible_divisor +=1

print max(factor_descomposition(600851475143))