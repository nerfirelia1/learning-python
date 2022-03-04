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
"""
"""
lista=["czerwony", "niebieski","","zielony", "", "brązowy"]
def funkcja(x):
    for i in x:
        if i == "":
            lista.remove(i)
    return x
print(funkcja(lista))

a = "aBC34$%,asBy03??"
def zwroc(x):
    b = ""
    for i in x:
        j=i.isalpha()
        if j==True:
            b=b+i
    return b
print(zwroc(a))

samochod={"marka":"Ford","model":"mustang","rok":1965}
print(samochod)
klucze=["dziesięć","dwadzescia","trzydziesci","czterdziesci"]
wartosci=[10,20,30,40]
slownik=dict(zip(klucze,wartosci))
print(slownik)
slownik2=dict()
for i in range(len(klucze)):
    slownik2.update({klucze[i]:wartosci[i]})
print(slownik2)
klasa={
    "klasa":{
        "imie":"Adam","oceny":{
            "Matematyka":5,
            "Polski":3
        }
    }
}

print(klasa)
zbior1={1,2,3,4,5}
zbior2={3,4,5,6,7}
print(zbior1.intersection(zbior2))
print(zbior1.union(zbior2))
print(zbior1.symmetric_difference(zbior2))
print(zbior1.difference(zbior2))
zbior1.difference_update({1,2,3})
print(zbior1)

krotka=(1,2,3,4,5)
print(krotka)
krotka=krotka[::-1]
print(krotka)
krotka2=([10,20,30],(5,15,25))
print(krotka2[0])
print(krotka2[1][0])
krotka3=("jabłko",[10,20,30],(5,15,25))
print(krotka3[1][2])
print(krotka3[2][1])
krotka4=(50)
print(krotka4)
krotka5=(1,2,3,4)
a,b,c,d=krotka5
print(a,b,c,d)
"""
"""
def funkcja(a):
    if a==2:
        return True
    if a>1:
        for i in range(2,a):
            if a%i==0:
                return False
            return True

    return False
#print(funkcja(7))

def funkcja1(x):
    a=0
    if x>0:
        for i in range(1,x):
            if x%i==0:
                a=a+i
        if x==a:
            return True
        else:
            return False
    return False
print(funkcja1(13))

def czynnikipierwsze(x):
    if x > 0:
        k=2
        while x!=1:
            while x%k==0:
                print(k)
                x=x//k
            k=k+1

czynnikipierwsze(120)
"""
def nwd(a,b):
    while a!=b:
        c=max(a,b)
        d=min(a,b)
        r=c-d
        e = max(r,d)
        f = min(r,d)
        a=e
        b=f
    return a
#print(nwd(1000,1))
"""
def nwd1(a,b):
    while b>0:
        r = a%b
        a=b
        b=r
    return a
print(nwd1(1000,1))

def nwd2(a,b):
    if b==0:
        return a
    return nwd2(b,a%b)

print(nwd2(1000,1))

def nww(a,b):
    return (a*b)//nwd2(a,b)
print(nww(12,24))
"""

"""
def funkcja(x,y):
    lista = []
    i=0
    while x>0:
        while y[i]<=x:
            lista.append(y[i])
            x-=y[i]
        i=i+1
    return lista
lista1=[500,200,100,50,20,10,5,2,1]
print(funkcja(49,lista1))
"""
"""
lista=[6,5,7,4,8,3,9,2,1]
def bubble(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-i-1):
            if  lista[j]> lista[j+1]:
                lista[j+1],lista[j]=lista[j],lista[j+1]
    return lista
print(bubble(lista))
#zrobic od lewo i od prawo itd
"""

#lista=[6,5,7,4,8,3,9,2,1]
"""
#zrobic na maxi tu na dole
def wybor(lista):
    for i in range(len(lista)):
        mini=i
        for j in range(i+1,len(lista)):
            if lista[mini] > lista[j]:
                mini=j
        lista[i],lista[mini]=lista[mini],lista[i]
    return lista
print(wybor(lista))
"""
lista=[6,5,7,4,8,3,9,2,1]
def insertion(lista):
    for i in range(1,len(lista)):
        liczba=lista[i]
        while i>0 and lista[i-1] > liczba:
            lista[i]=lista[i-1]
            i=i-1
        lista[i]=liczba
    return lista
print(insertion(lista))

def palindrom(x):
    i=0
    j=len(x)-1
    while i<j:
        if x[i]==x[j]:
            i = i + 1
            j = j - 1
        else:
            return "nie"
    return "tak"
print(palindrom("kajakak"))
def palindrom2(x):
     x2=x[::-1]
     if x==x2:
         return True
     return False
print(palindrom2("kajako"))

def anagram(x,y):
    if sorted(x)==sorted(y):
        return True
    return False
print(anagram("matura", "traumay"))