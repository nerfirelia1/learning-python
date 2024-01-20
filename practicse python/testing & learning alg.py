
def czy_pierwsza(n):
    for i in range(2,n):
        if n%i==0:
            return "Nie"
    return "Tak"

def czynniki(x):
    czynniki=[]
    i=1
    while x>1:
        i=i+1
        while x%i==0:
            czynniki.append(i)
            x=x/i
    return czynniki

print(czynniki(147))

