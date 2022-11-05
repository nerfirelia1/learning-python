from ast import pattern
from sys import platlibdir
import math

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


def Cezar(tekst: str, klucz: int) -> str:
    tekst = list(tekst)
    wynik = ""
    for i in tekst:
        if ord(i) >= 65 and ord(i) <= 90:
            wynik += chr((ord(i) + klucz - 65) % 26 + 65)
        elif ord(i) >= 97 and ord(i) <= 122:
            wynik += chr((ord(i) + klucz - 97) % 26 + 97)
        else:
            wynik = wynik + i
    return wynik


# Szyfrować musimy tylko duże i małe litery w szyfrze cezara
# dla dużych 65-90, -65  i 26%.
# dla małyc liter 97-122, -97 i 26%.

print(Cezar("ABCXYZabcxyz Ala ma^psa, a Konrad:)ma kota", 8))


def zdziesietnegosystemu(n: int, system: int) -> str:
    wynik = ""
    while n > 0:
        r = n % system
        if r <= 9:
            wynik = wynik + str(r)
        else:
            wynik = chr(55 + r) + wynik
        n = n // system
    wynik = wynik[::-1]
    return wynik


print(zdziesietnegosystemu(1875, 3))


def NaDzies(n: str, sys: int) -> int:
    wyn = 0
    dl = 0
    for i in range(len(n) - 1, -1, -1):
        print(i)
        x = n[i]
        if ord(x) >= 48 and ord(x) <= 57:
            wyn += int(x) * sys ** dl
        elif ord(x) >= 65 and ord(x) <= 90:
            wyn += (ord(x) - 55) * sys ** dl
        elif ord(x) >= 97 and ord(x) <= 122:
            wyn += (ord(x) - 87) * sys ** dl
        dl += 1
    return wyn


print(NaDzies("12211", 3))


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


print(babelkowesortowanie([2, 6, 42, 57, 5, 2, 8, 3, ]))
a = "nosiema"
print(len(a))


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
