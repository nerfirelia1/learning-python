def doskonała(x):
    suma=0
    for i in range(1,x):
        if x%i==0:
            suma+=i
    if suma==x:
        return True
    return False
print(doskonała(6))

def czyniikipierwsze(x):
    y=2
    czynniki=[]
    while x>1:
        if x%y==0:
            while x%y==0:
                czynniki.append(y)
                x=x/y
        y=y+1
    return czynniki
print(czyniikipierwsze(81))
