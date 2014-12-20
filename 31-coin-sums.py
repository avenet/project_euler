def count_ways(coins, total):
    return _count_ways(0, coins, total)
    
def _count_ways(current, coins, total):
    if coins == []:
        return current == total and 1 or 0
    coin_value = coins[0]
    
    result = 0
    
    cant = 0
    while current + (coin_value * cant) <= total:
        result += _count_ways(current + (coin_value * cant), coins[1:], total)
        cant += 1
        
    return result
    
print count_ways([1,2,5,10,20,50,100,200], 200)
    