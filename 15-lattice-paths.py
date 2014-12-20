directions = [(0,1), (1,0)]
cache = {}

def ways(position, target):
    if position == target:
        return 1
    result = 0
    for direction in directions:
        new_position = (position[0]+ direction[0], position[1]+ direction[1])
        
        if new_position[0] <= target[0] and new_position[1] <= target[1]:
            ways_to_reach = cache.get(new_position)
            
            if not ways_to_reach:
                ways_to_reach = ways(new_position, target)
                cache[new_position] = ways_to_reach
            
            result += ways_to_reach
            
    return result
    
    
print ways((0,0), (20,20))