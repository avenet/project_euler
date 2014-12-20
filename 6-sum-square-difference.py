def sum_square_difference(n):
    number_square_sum = (n*(n+1)/2)**2
    square_num_sum = sum([x**2 for x in range(1,n+1)])
    return number_square_sum - square_num_sum
    
print sum_square_difference(100)