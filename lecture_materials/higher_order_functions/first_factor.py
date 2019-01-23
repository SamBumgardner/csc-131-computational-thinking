def firstFactor(n):
    factor = 2  
    while n % factor != 0:
        factor +=1
    return factor 

a = [125, 147, 143, 289]
print(list(map(firstFactor, a)))
