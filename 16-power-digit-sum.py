number = 2**1000
string_number = str(number)
print reduce(lambda x,y: int(x)+int(y), string_number)