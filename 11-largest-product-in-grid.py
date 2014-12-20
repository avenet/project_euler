from __future__ import with_statement

matrix = []

with open("matrix.txt", "r") as f:
    for line in f:
        matrix.append([int(x) for x in line.split() if x])

directions = [(0,1),(0,-1),(1,0), (1,-1), (1,1), (-1,0), (-1,1), (-1,-1)]

max_product = 0

def in_range(x, y):
    return x>=0 and y>=0 and x<20 and y<20
    
for x in range(20):
    for y in range(20):
        for direction in directions:
            product = matrix[x][y]
            if in_range(x + 3*direction[0], y+ 3*direction[1]):
                for factor in range(1, 4):
                    current_x = x + factor*direction[0]
                    current_y = y + factor*direction[1]
                    product *= matrix[current_x][current_y]
                max_product = max(max_product, product)
                
print max_product