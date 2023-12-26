from ast import pattern
from sys import platlibdir
def pierwsza(x:int) -> bool:
    if x==1 or x==2:
        return True
    for i in range(2,x):
        if x%i==0:
            return False
    return True
print(pierwsza(179))


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
print(zdziesietnegosystemu(10,2))
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
print(palindrom("Kajak"))
liczby0=[]
liczby=[0,0,0,0,0,0]
while len(liczby0)<=20:
    losujliczbe=randint(1,6)
    liczby0+=[losujliczbe]
    if losujliczbe in liczby0:
        liczby[losujliczbe-1]+=1
print(liczby)
print(liczby0)
def f(x: float) -> float:
    return 2*x*x*x - 2*x - 8
def bisekcja(a:float,b:float,eps:float)->float:
    if f(a) * f(b) >0:
        return None
    while b-a>=eps:
        c = (a + b) / 2
        if c == 0:
            return c
        if f(a) * f(c) < 0:
            b=c
        else:
            a=c
    return c
print(bisekcja(-2, 5, 0.0001))
def char_tab(tab: str) -> str:
    tab=list(tab)
    for i in range(len(tab)):
        for j in range(len(tab) - i - 1):
            if tab[j] > tab[j + 1]:
                 tab[j+1], tab[j] = tab[j], tab[j+1]
    return "".join(tab)
print(char_tab("3246453"))
print(char_tab("n//>o seima"))

def sortowaniebabelkowe(lista:list)->list:
    for i in range(len(lista)):
        for j in range((len(lista)-i)-1):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return lista

lista=[12,7,3,90,4]
print(sortowaniebabelkowe(lista))

def bisekcja(x:float,y:float,eps:float)->float:
    if f(x)*f(y)>0:
        return None
    while y-x>=eps:
        c=(x+y)/2
        if c==0:
            return c
        if f(x) * f(c):
            y=c
        else:
            x=c
    return c

def sortowaniebabelkowe(lista:list)->list:
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return lista
print(sortowaniebabelkowe([2,7,5,2,4,1,1]))

def sortowaniewybor(lista:list)->list:
    for i in range(len(lista)):
        min=i
        for j in range(i+1,len(lista)):
            if lista[min]<lista[j]:
                min=j
        lista[j],lista[min]=lista[min],lista[j]
    return lista

print(sortowaniewybor([2,7,5,2,4,1,1]))

def bisekcja(a:float, b:float, eps:float) -> float:
    if f(a)* f(b)>0:
        return None
    while b-a>= eps:
        c=(a+b)/2
        if c==0:
            return c
        elif f(a) * f(c) <0:
            b=c
        else:
            a=c
    return c

def insertion(lista:list)-> list:
    for i in range(1,len(lista)):
        liczba=lista[i]
        while i>0 and lista[i]>lista[i-1]:
            lista[i-1]=lista[i]
            i=i-1
        lista[i]=liczba
    return lista
def insertion_sort(tab: list) -> list:
    for i in range(1, len(tab)):
        liczba = tab[i]
        while i > 0 and tab[i-1] > liczba:
            tab[i] = tab[i-1]
            i -= 1
        tab[i] = liczba
    return tab

print(insertion_sort([2,7,43,1,14,7]))


def NaDziesietny(n:str, system:int)-> int:
    wynik=0
    dlugosc=len(n)-1
    for i in n:
        if int(i) <=9:
            wynik+= int(i)* system**dlugosc
        else:
            wynik+=ord(i)*system**dlugosc
        dlugosc=dlugosc-1
    return wynik
print(NaDziesietny("334",5))

def NaDzies(n: str, sys: int) -> int:
    wyn = 0
    dl = len(n) - 1
    for x in n:
        if ord(x) >= 48 and ord(x) <= 57:
            wyn += int(x) * sys ** dl
        elif ord(x) >= 65 and ord(x) <= 90:
            wyn += (ord(x) - 55) * sys ** dl
        elif ord(x) >= 97 and ord(x) <= 122:
            wyn += (ord(x) - 87) * sys ** dl
        dl -= 1
    return wyn
print(NaDzies("334",5))


print(a[::-1])


def rysuj(x):
    if 2*x<=10:
        a=2*x
        print(a)
        return rysuj(2*x)
    if 2*x+1<=10:
        b=2*x+1
        print(b)
        return rysuj(2*x+1)
rysuj(1)

def insertion_sort(lista:list)->list:
    for i in range(1,len(lista)):
        liczba=i
        while i>0 and lista[i-1]>lista[i]:
            lista[i-1]=lista[liczba]
            i=i-1
        i=liczba
    return lista
print(insertion_sort([2,7,45,1,3,5]))

#POWTORKA WSZYSTKO NARAZ

def lczpierwsza(x:int)->bool:
    if x<=1:
        return False
    for i in range(2,len(x)-1):
        if x% i ==0:
            return False
    return True


tab = []
for i in range(101):
    tab.append(True)



def sito(a: int, b: int, tab: list) -> list:
    tab[0] = False
    tab[1] = False
    for i in range(2, int(b ** 0.5) + 1):
        if tab[i] == True:
            j = i * 2
            while j <= b:
                tab[j] = False
                j += i
    for i in range(a, b + 1):
        if tab[i]:
            print(i, "jest liczba pierwsza")
    return tab
sito(10,100,tab)

def sortowanie(x,y):
    x1=list(x)
    for i in range(len(x1)):
        for j in range(len(x1)-i-1):
            if x1[j]>x1[j+1]:
                x1[j],x1[j+1]=x1[j+1],x1[j]
    x2="".join(x1)
    y1=list(y)
    for k in range(len(y1)):
        for z in range(len(y1)-k-1):
            if y1[z] > y1[z+1]:
                y1[z],y1[z+1]=y1[z+1],y1[z]
    y2="".join(y1)
    print(x2,y2)
    if x2==y2:
        return True
    return False
print(sortowanie("matura","traumaa"))
print(sortowanie("maturaa","trauma"))


def sqrt(n):
    snd = n/2
    while math.fabs(snd - n/snd) > 0.000001:
        snd = float((snd + n/snd)/2)
        if snd*snd == n:
            break
    return round(snd, 3)
print(sqrt(40-20))