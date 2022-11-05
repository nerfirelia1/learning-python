from random import randint
#-------------------------------FUNKCJE-----------------------------
def silnia(n):
    if n>1:
        return n * silnia(n - 1)
    else:
        return 1
def dodawaniee(a):
    if a >0:
        return a+dodawaniee(a-1)
    else:
        return a
print(dodawaniee(8))
print(dodawaniee(4))
s=0
x=0
a=0
n = int(input("Podaj liczbe: "))

#------------------------------PĘTLE--------------------------------------------
while (n>0):
    x=n%10
    s=s+1
    a=a+x
    n=n//10
print("Liczba składa się z tylu liczb: ",s, "suma liczb wynosi: ", a)

a=0
for i in range(1,6):
    a=a+1
    for x in range(i):
        print(i, end=" ")
    print()

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(lista[-1])
for liczba in lista[0::3]:
    print(liczba, end=" ")
liczby = [5, 6.5, 7, 8, 9, 10]

print(liczby[-1])


#---------------------------SORTOWANIE-------------------------------------------

lista1=[8,2,1,9,5,10,12]
i=1
a=lista1[i]

def wstawianiesortowanie(x):
    while i <len(lista1):
        a = lista1[i]
        j=i-1
        while j>=0 and a < lista1[j]:
            lista1[j+1] = lista1
            j=j-1
        lista1[j+1] = a

#---------------------------------Liczba pierwsza,NWW,NWD,i inne takie--------------------------------------------------

def sprawdzP(x):
    if x==2 or x==1:
        return "Ta liczba jest liczbą pierwszą"
    for i in range(2,x):
        if x%i==0:
            return "ta liczba nie jest liczbą pierwszą"
        else:
            return "Ta liczba jest liczbą pierwszą."

print(sprawdzP(3))

def NWD(x,y):
     while x!=y:
        c=max(x,y)
        d=min(x,y)
        r=c-d
        e=max(r,d)
        f=min(r,d)
        x=e
        y=f
        return x

def funkcja1(x):
    a=0
    if x>0:
        for i in range(1,x):
            if x%i==0:
                a=a+1
        print(a,x)
        if x==a:
            return True
        else:
            return False
    return False
print(funkcja1(6))

for i in range(1,10):
    print(i)

print(3%8)