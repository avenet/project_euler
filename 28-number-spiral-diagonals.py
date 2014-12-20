def sum_numbers(spiral_size):
    square_size = 1
    n = 1
    sum_of_numbers = 1
    current_number = 1
    
    while n < spiral_size:
        n+=2
        right_down, left_down, left_up, left_rigth = 0,0,0,0
        right_down = current_number + n - 1
        left_down = right_down + n - 1
        left_up = left_down + n - 1
        right_up = left_up + n - 1
        
        sum_of_numbers += (right_down + left_down + left_up + right_up)
        current_number = right_up
    return sum_of_numbers
    
print sum_numbers(1001)