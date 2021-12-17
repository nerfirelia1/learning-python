"""
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

for x in range(1,11):
    for i in range(1,11):
        print(x*i, end=" ")
    print()
"""
