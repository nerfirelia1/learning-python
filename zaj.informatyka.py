
def iloczynsuma(x,y):
    if x*y>1000:
        return x + y
    else:
        return x*y
print (iloczynsuma(20,30))
print(iloczynsuma(40,30))

def func():
    for x in range(1,11):
        y = x-1
        z = y + x
        print("obecna liczba to: ", x, ", poprzednia liczba to: ", y, ", suma liczb: ", z)
func()

a = input("Podaj słowo: ")
print(a)
długość = len(a)
for x in range(0,długość,4):
    print(a[x])


def func1(x):
    a=x[0]
    b=x[-1]
    if a == b:
        return True
    else:
        return False

lista = [10,20,30,40,10]
print(func1(lista))

lista2=[10,20,30,40,50]
print(func1(lista2))

lista3 = [10,20,33,46,55]
def wypisz(x):
    for liczba in lista3:
        if liczba % 5 ==0:
            print(liczba)

wypisz(lista3)

a = "Lubię jezyk Python, dlatego uczę się języka Python"
ile = a.count("Python")
print(ile)
ile2 = a.count("e")
print(ile2)
"""
"""
i=0
x=0
for i in range(1,6):
    for x in range(i):
        print(i, end=" ")
    print()
"""
"""
a = int(input("podaj liczbe: "))
liczbaoryginalna = a
palindromiczna=0
while a>0:
    x = a%10
    palindromiczna = palindromiczna*10 + x
    a=a//10
if palindromiczna == liczbaoryginalna:
    print("Liczby są te same")
else:
    print("liczby są różne")


b = int(input("podaj liczbe:"))
liczba = b
while b>0:
    x = b%10
    print(x, end=" ")
    b = b//10

for x in range(1,12):
    for i in range(1,12):
        print(x*i, end=" ")
    print()


for i in range(1,6):
    for x in range(i,6):
        print("*", end=" ")
    print()

a = int(input("Podaj liczbe: "))
n = int(input("podaj n: "))
wynik = 1
for i in range(n):
    wynik = wynik * a
print(wynik)


print("jestem","Adam",sep="**")
liczba = 123.45678
print("%.3f" % liczba)


lista = []
for i in range(1,6):
    a = float(input("podaj element: "))
    lista.append(a)
print(lista)


imie1, imie2, imie3 = input("imie: ").split()
print(imie1,imie2,imie3)


suma=0
n=10

for i in range(0,n+1):
    suma =suma+i
print(suma)


liczby = [12,15,75,78,150,152,155,365,369,45,525,50]
for liczba in liczby:
    if liczba % 5==0 and liczba<=150:
        print(liczba)
    elif liczba >500:
        break


x = int(input("podaj liczbe: "))
suma = 0
licznik = 0
while  x > 0:
    a = x%10
    suma = suma+a
    licznik = licznik+1
    x= x//10
print(suma,licznik)


for i in range(1,6):
    a = 6-i
    for x in range(i,6):
        print(a, end=" ")
        a = a-1
    print()

for i in range(-10,0):
    print(i)


for i in range(-1,-11,-1):
    print(i)
for i in range(10,0,-1):
    print(i)
for i in range(10,0,-2):
    print(i)
for i in range(17,0,-5):
    print(i)



start = 0
koniec = 100

for i in range(start,koniec+1):
    if i > 1:

        for x in range(2,i):
            if  i%x==0:
                break
        else:
            print(i)


a=0
b=1
for i in range(1,22):
    print(b)
    pomocniczna = a+b
    a=b
    b=pomocniczna
#ciąg Fibonacciego

b = 1
a = int(input("Podaj liczbe: "))
if a<0:
    print("nie istnieje silnia z liczby ujemnej")
else:
    for i in range(1,a+1):
        b = b*i
    print(b)


liczba = int(input("Podaj liczbe: "))
suma = 0
while liczba >0:
    a = liczba%10
    suma=suma*10+a
    liczba = liczba//10
print(suma)


lista = [10,20,30,40,50,60,70,80,90,100]
for liczba in lista[1::2]:
    print(liczba, end=" ")

liczba = int(input("liczba: "))
for i in range(1,liczba+1):
    print(i**3)


for i in range(1,6):
    for x in range(1,i+1):
        print("*", end=" ")
    print()
for y in range(1,5):
    for z in range(5,y,-1):
        print("*", end=" ")
    print()

a = int(input("Podaj n: "))
wynik=1
for i in range(1,a+1):
    wynik = wynik *i
print("silna od N wynosi: ", wynik)

n = int(input("Podaj długość choinki "))
for i in range(1,n+1):
    for x in range(n,i-1,-1):
        print("*", end=" ")
    print()

n = int(input("Podaj n: "))
silnia=1
for i in range(1,n+1):
    silnia = silnia * i
print(silnia)

b = int(input("podaj liczbe:"))
while b>0:
    x = b%10
    print(x, end=" ")
    b = b//10

