def factorial(n):
    result = 1
    for x in range(1, n+1):
        result *= x
    return result
    
one_hundred_factorial = factorial(100)
factorial_string = str(one_hundred_factorial)
factorial_digits = [int(x) for x in factorial_string]
print sum(factorial_digits)