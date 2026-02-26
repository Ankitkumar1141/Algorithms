def power(a,b):   # a: base ; b: exponent
    val=0
    if(b==0):
        return 1
    val = a * power(a,b-1)
    return val

print(power(3,4))
    