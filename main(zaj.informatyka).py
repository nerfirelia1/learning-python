def iloczynsuma(x,y):
    if x*y>1000:
        return x + y
    else:
        return x*y
#print (iloczynsuma(20,30))
#print(iloczynsuma(40,30))

def func():
    for x in range(1,11):
        y = x-1
        z = y + x
        print("obecna liczba to: ", x, ", poprzednia liczba to: ", y, ", suma liczb: ", z)
func()
"""
a = input("Podaj słowo: ")
print(a)
długość = len(a)
for x in range(0,długość,2):
    print(a[x])
"""

def func1(x):
    a=x[0]
    b=x[-1]
    if a == b :
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


