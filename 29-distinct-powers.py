powers = list()
for a in xrange(2, 101):
    for b in xrange(2, 101):
        powers.append(a**b)
        
print len(set(powers))