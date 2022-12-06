from ast import pattern
from sys import platlibdir
from random import randint
import math
print(3)
"""
def pierwsza(x: int) -> bool:
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
print(pierwsza(20))

def f(x: float) -> float:
    return 2*x*x*x - 2*x - 8


def bisekcja(a: float, b: float, eps: float) -> float:
    if f(a) * f(b) > 0:
        return None
    while b-a >= eps:
        c = (a+b)/2
        print(c)
        if(c) == 0.0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

print(bisekcja(-2, 5, 0.0001))

def palindrom(string: str) -> bool:
    lista = list(string)
    if lista == lista[::-1]:
        return True
    return False


#iteracyjnad droga

def palindrom1(string:str)-> bool:
    i=0
    j=len(string)-1
    while i<j:
        if string[i]!=string[j]:
            return False
        i=i+1
        j=j-1
    return True
print(palindrom1("kajak"))

#ASCII
print(ord('A'))
print(chr(65))
def nwd1(a,b):
    while b>0:
        r = a%b
        a=b
        b=r
    return a
print(nwd1(1000,1))
print(nwd1(119,187))
"""
print("no eloo")
# Szyfrować musimy tylko duże i małe litery w szyfrze cezara
# dla dużych 65-90, -65  i 26%.
# dla małyc liter 97-122, -97 i 26%.
print(5)




def zdziesietnegosystemu(n:int,system:int) -> str:
    wynik =""
    while n>0:
        r=n%system
        if r >=10:
            wynik = wynik + chr(r+55)
        else:
            wynik = wynik + str(r)
    wynik = wynik[::-1]
    return wynik

# 48 - 57 dla cyfer 0-9
# 65 - 90 dla liter dużych (-55)
# 97 - 122 dla liter małych (-87)


def znajdznajmniejszaoraznajwiekszaliczbewliscie(lista: list) -> tuple:
    min = lista[0]
    max = lista[0]
    for i in lista:
        if i < min:
            min = i
        if i > max:
            max = i
    return (min, max)


def pierw(n: float, eps: float) -> float:  # newton - rhapson
    a = 1.0
    b = n
    while math.fabs(a - b) >= eps:
        # print((a+b)/2)
        a = (a + b) / 2
        b = n / a
    return (a + b) / 2


print(pierw(3, 0.001))


def palindromek(n: str) -> bool:
    i = 0
    j = len(n) - 1
    while i < j:
        if n[i] != n[j]:
            return False
        i = i + 1
        j = j - 1
    return True


print(palindromek("kajaasdk"))



def babelkowesortowanie(n: list) -> list:
    for i in range(len(n)):
        for j in range(len(n) - 1 - i):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
    return n

def wybor(lista):
    for i in range(len(lista)):
        mini=i
        for j in range(i+1,len(lista)):
            if lista[mini] > lista[j]:
                mini=j
        lista[i],lista[mini]=lista[mini],lista[i]
    return lista


print(babelkowesortowanie([2, 6, 42, 57, 5, 2, 8, 3, ]))
a = "nosiema"
print(len(a))
tab=[2,5,7,5,4,6]
#-------------------------sortowania-------------------------------
for i in range(len(tab)):
    print(tab[i])
#bąbelkowe
def bubble(n: list) -> list:
    for i in range(len(n)):
        for j in range(len(n) - 1 - i):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
    return n

#insertion
def insertion(lista:list)-> list:
    for i in range(1,len(list)):
        liczba = lista[i]
        while i>0 and lista[i-1] > liczba:
            lista[i] = lista[i-1]
            i=i-1
        lista[i] = liczba
    return lista



#przez wybór
def selection_sort(lista:list) -> list:
    for i in range(len(lista)):
        min = i
        for j in range(i+1,len(lista)):
            if lista[min]>lista[j]:
                min = j
        lista[min],lista[i]=lista[i],lista[min]
    return lista


print(selection_sort([2,6,3,1,45,45657,4]))

#-------------------------------------------------------------------
def NWD(x, y):
    while y > 0:
        r = x % y
        x = y
        y = r
    return x


print(NWD(32, 24))


def nwd_iter(a: int, b: int) -> int:
    while b > 0:
        a, b = b, a % b
    return a


print(nwd_iter(32, 24))

def nww(a, b):
    return a*b//nwd_iter()
sesses=[2,5,7,5,4,6]
for i in range(len(sesses)):
    print(sesses[i])

def pierw(n: float, eps: float) -> float: #newton rhapson
    a= 1.0
    b = n
    while math.fabs(a-b)>= eps:
        a = (a+b)/2
        b = n/a
    return(a+b)/2
print(pierw(30,0.002))

def f(x: float) -> float:
    return 2*x*x*x - 2*x - 8

def bisekcja(a:float, b:float, eps:float) -> float:
    if f(a) * f(b) > 0:
        return None
    while b-a >= eps:
        c = (a+b)/2
        if c == 0.0:
            return c
        if f(a) * f(c) < 0:
            b=c
        else:
            a=c
    return c
def palindrom(word:str) -> bool:
    a=0
    b=len(word)-1
    while a<b:
        for i in range(1,len(word)):
            if word[a] != word[b]:
                return False
            a=a+1
            b=b-1
    return True
print(palindrom("koń"))
liczby0=[]
liczby=[0,0,0,0,0,0]
while len(liczby0)<=20:
    losujliczbe=randint(1,6)
    liczby0+=[losujliczbe]
    if losujliczbe in liczby0:
        liczby[losujliczbe-1]+=1
print(liczby)
print(liczby0)