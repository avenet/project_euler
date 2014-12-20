def fibo_iterator(max_number):
    first = 0
    second = 1
    while first + second < max_number:
        yield first + second
        first, second = second, first + second
        
print sum([x for x in fibo_iterator(4000000) if x%2==0])