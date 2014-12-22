for a in range(1000):
    for b in range(a, 1000):
        c = 1000 - b - a
        if a+b <= 1000 and c > b:
            if a**2 + b**2 == c**2 and (a+b+c) == 1000:
                print a*b*c