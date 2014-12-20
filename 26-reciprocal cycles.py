sequence_length = 0
max_value = 0
 
for i in xrange(1000, 1, -1):
    if sequence_length >= i:
        break
 
    found_remainders = [0 for x in range(i)]
    value = 1
    position = 0
 
    while (found_remainders[value] == 0 and value != 0):
        found_remainders[value] = position
        value *= 10
        value %= i
        position+=1
 
    if (position - found_remainders[value] > sequence_length):
        sequence_length = position - found_remainders[value]
        max_value = i
        
print max_value

