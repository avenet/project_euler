def factorial(n):
    if n == 0:
        return 1
    return reduce(lambda x,y: x*y, range(1, n+1))
    
desired_permutation = 10**6 - 1

def decompose(n):
    k = 0
    while True:
        if factorial(k) >= n:
            break
        k+=1
    result = ""
    for i in range(k-1,-1,-1):
        result += str(n/factorial(i))
        n = n % factorial(i)
    return result

desired_descomposition = decompose(desired_permutation)

numbers = [str(x) for x in range(10)]

permutation = ""

for str_number in desired_descomposition:
    index = int(str_number)
    permutation += numbers[index]
    print numbers, index, numbers[index]
    del numbers[index]
    
print permutation