def collatz_sequence_length(number):
    l = 1
    while number != 1:
        if number %2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        l+=1
    return l
    
number = 1
longest_length = 0
answer = 1

while number < 10**6:
    collatz_length = collatz_sequence_length(number)
    if collatz_length > longest_length:
        answer = number
        longest_length = collatz_length
    number += 1
    
print answer