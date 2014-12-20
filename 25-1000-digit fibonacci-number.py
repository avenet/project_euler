def fibo_iterator():
    f,s = 1,1
    while True:
        yield f
        f,s = s, f+s
    
    
for i, fibo in enumerate(fibo_iterator()):
    if len(str(fibo)) == 1000:
        print i+1
        break