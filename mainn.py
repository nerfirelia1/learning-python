"""
from math import sqrt
from math import pi
from random import randint
from random import uniform
from math import pi as liczbapi

#-------------------------- funkcje wprowadzenie-----------------------------------------
def potegowanie(x,y):
    return x**y
print("2 do 5 = ")
print(potegowanie(2,5))

a = potegowanie(1,4)
print(a)

#------------------------------------------------ rekurencja --------------------------------------------------------

def func(x):
    return x * x

def func2(f1,x):
    return f1(x) * x
print(func2(func,5))

def silnia (x):
    if x <= 1:
        return 1
    else:
        return x * silnia(x - 1)

print(silnia(5))
print(silnia(3))

#----------- cwiczenia poczontkujonce---------------

#zadanie 3
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
print("suma a i b wynosi: ", a+b)
print("rurznica a i b wynosi: ", a-b)
print("Iloczyn a i b wynosi: ", a*b)
print("Iloraz a i b wynosi: ", a/b)
print("pierwiastek z a+b wynosi: ", sqrt(a+b))
print("a do b oraz b do a wynosi: ", a**b , b**a)

#zadanie 5
r = int(input("podaj promien kola(r): "))
print("pole kola wynosi: ", pi * (r*r))
print("obwud kola wynosi: ",2 * pi * r)

#zadanie 6
a =  randint(0,10)
zgadnij = int(input("zgadnij jaka to liczba, z zakresu od 0 do 10: "))
while zgadnij != a:
    if zgadnij < a:
        print("To za malo sprubuj jeszcze raz")
    elif zgadnij > a:
        print("to za duzo sprubuj jeszcze raz: ")
    zgadnij = int(input("zgadnij jaka to liczba, z zakresu od 0 do 10: "))

print("brawo zgadnoles")
print("odpowiedz to: " , a)

#zadanie 10
a =  uniform(3,16)
print(a)

#zadania listy
a = [2,4,10,64]
print(a[0])
x = a[0]
y = a[3]
xy =[x, y]
print(xy)


#-------------------------wyjatki (try,except) -----------------------------------------
try:
    print(4/0)
    print(x+"asd")
    lista=[]
except (TypeError, ZeroDivisionError):
    print("wystąpił błąd")
except IndexError:
    print("nie istnieje taka lista")
"""


