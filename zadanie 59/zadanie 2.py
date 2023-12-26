liczby=[]
#1
with open("liczby.txt") as file:
    for line in file:
        liczby.append(int(line))
"""def rozkladnaczyn(x: int):
    czynniki=[]
    #while x>1:
    k=2
    while x>1:
        if x%2==0:
            break
        while x%k==0:
            czynniki.append(k)
            x=x//k
        k=k+1
    return czynniki
#print(rozkladnaczyn(25))
nieparzysta=0
for i in liczby:
    zbior=set()
    for j in rozkladnaczyn(i):
        zbior.add(j)
    if len(zbior) == 3:
        nieparzysta+=1
        print(nieparzysta)
print(nieparzysta)
"""
#zadanie 2
liczby1=[]
for i in liczby:
    a=str(i)
    liczby1.append(int(a[::-1]))
def palindrom(x):
    x=str(x)
    l=0
    r=len(x)-1
    while l<=r:
        if x[l]!=x[r]:
            return False
        l=l+1
        r=r-1
    return True
liczby2=[]
sumapalindrom=0
for j in range(len(liczby1)):
    if palindrom(liczby1[j]+liczby[j])==True:
        sumapalindrom+=1
print(sumapalindrom)

#zadanie 3

def moc(x):
    m=0
    while x>9:
        iloczyn=1
        while x>0:
            iloczyn=iloczyn*(x%10)
            x=x//10
        m+=1
        x=iloczyn
    return m
moce=[0]*9
min=9999999
max=0
for i in liczby:
    a=moc(i)
    moce[a]+=1
    if a==1:
        if i<min:
            min=i
        elif i>max:
            max=i
with open("wyniki59.txt","w") as file:
    file.write("zad3"+"\n")
    for i in range(1,9):
        file.write(str(moce[i])+"\n")
    file.write(str(min)+"\n")
    file.write(str(max)+"\n")






