def can_be_written(number, power):
    number_powers = [int(digit)**power for digit in str(number)]
    return sum(number_powers) == number
    
total_sum = 0
for n in xrange(2, 10**6):
    if can_be_written(n, 5):
        total_sum += n

print total_sum