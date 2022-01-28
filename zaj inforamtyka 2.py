"""
b = int(input("podaj liczbe:"))
while b>0:
    x = b%10
    print(x, end=" ")
    b = b//10

def silnia(n):
    if n > 1:
        return n*silnia(n-1)
    return 1

def dodawanie(a):
    if a>0:
        return a+dodawanie(a-1)
    else:
        return a
print()
print("silnia wynosi: ",silnia(5))
print("dodawanie kolejnych n wynosi: ",dodawanie(10))
"""

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
print(fibonacci(10))

def potęgowanie(x,y):
    w=x
    if y==0:
        return 1
    else:
        for i in range(y-1):
            x=w*x
        return x
print(potęgowanie(2,6))

def dodawaniee(x,y):
    return x+y
print(dodawaniee(5,7))

def operacje(x,y):
    z = x**2
    z=z+dodawaniee(x,y)
    return z
print(operacje(3,4))


def delta(a,b,c):
    return b**2-4*a*c

def funkcja(a,b,c):
    if  delta(a,b,c)>0:
        z=delta(a,b,c)**0.5
        v=(-b-z)/(2*a)
        f=(-b+z)/(2*a)
        return v,f
    elif delta(a,b,c) ==0:
        n= -b/(2*a)
        return n
    else:
        return "sprzeczność"
print(funkcja(1,1,0))
print(funkcja(1,2,1))
print(funkcja(1,2,2))

lista =[12,5,189,64,34,100,655,34,2,6,5,198,598]

def znajdz():
    a=lista[0]
    for i in lista:
        if i>a:
            a=i
    return a
print(znajdz())

#------------------------------------STRING---------------------------------------------


slowo = "komputerr"
a = slowo[0] + slowo[4] + slowo[8]
print(a)



def znajdz1(x):
    a=len(x)//2
    return x[0],x[a], x[-1]

print(znajdz1("informatyka"))
print(znajdz1("kamil"))

def znajdz2(a,b):
    return a[0],b[0],a[len(a)//2], b[len(b)//2], a[-1], b[-1]
print(znajdz2("komputer", "telefon"))

a = "BacdEFghIOppQ"
def funkcja(x):
    a=""
    b=""
    for i in x:
        if i.islower():
            a=a+i
        else:
            b=b+i
    return a+b
print(funkcja(a))
c = "AsdEE^**34,,As*,.?{{^%ac34"
def licz(x):
    a=0
    b=0
    c=0
    for i in x:
        if i.isalpha():
            a=a+1
        elif i.isdigit():
            b=b+1
        else:
            c=c+1
    return a,b,c
print(licz(c))

def funkcja1(x,y):
    y=y[::-1]
    a=""
    for i in range(len(x)):
        a=a+x[i]
        a=a+y[i]
    return a
print(funkcja1("kon","mal"))

def funkcja2(x,y):
    for i in y:
        if i not in x:
            return False
    return True
print(funkcja2("adam", "dma"))
print(funkcja2("telewizor", "iowf"))

a = "mój kot ma na imie Burek, Kot lubi jeść, kot lubi spać"
def wylicz(x):
    s1=x.lower()
    licznik=s1.count("kot")
    return licznik
print(wylicz(a))
b = "As45,,aBr5%%,90p?"
def wylicz1(x):
    suma=0
    licznik=0
    for i in x:
        if i.isdigit():
            suma=suma+int(i)
            licznik=licznik+1
    srednia=suma/licznik
    return suma,srednia
print(wylicz1(b))

a ="Ala-ma-kota"
def wypisz(x):
    b=x.split("-")
    for i in b:
        print(i)
wypisz(a)
