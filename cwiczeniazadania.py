from random import randint
""""
def hello(name):
    print(f"Hello {name}")


name = "John"

hello("Jasiu")

print("Hello {}".format(name))

print("Hello " + name)


def awesome_func(x, y):
    return x**y


print(awesome_func(2, 4))

#------------------------------------------------cwiczenia z petlami ------------------------------

x=0
for x in range(0,4):
    print(x)
#1
    def wyswietl (a,z,e):
        a -= 2
        for a in range (a,z,e):
            a+=e
            print(a)


    wyswietl(1,2,3)

  #2

x = 0
for i in range (5):
    x = x+6
    print(x)

    #3
    y=0
    for i in range (5):
        y = y+i
        print(y)

    #5
    for z in range (52,57):
        z+=1
        print(z)

    #6
    for a in range (7):
        a+=1
        if a == 5:

            print("znalazłem 5!")
            continue


        print(a)

    #7
    for i in range (3):
        i =i+1
        print(i,"a")
        print(i , "b")
        print(i , "c")
    #8
    a = list(range(1,9))
    print(a)

    #9
    for i in a:
        if i == 5:
            break
        print(i)
    #10

    i =4
    while i < 19:
        i = i+2
        print(i)

    #11
lista = ["AA", "BBB","CCCC","DDDDD"]
for k in lista:
        print(k)
else:
    print("lista się skończyła",)

#12

for v in range(1,20):
    if v % 3 == 0:
        print(v)

#13
g=1
while g < 22:

    print(g)
    g=g+5
#14
x =10
while x >-1:
    print(x)
    x= x-1
h= 0
def licz(x,y):
    while (x<y):
        print(x)
        x = x+1

licz(4,9)


#15
# x = godziny
# y = minuty
# z = sekundy

z = int(input("Podaj sekundy: "))
x = z//3600
r = z%3600
y = r//60
r1 = z%60
print("godzin: ", x)
print("minut: ", y)
print("sekund: ", r1)
"""


x=0
for x in range(0,4):
    print(x)
a = int(input("Podaj długosc choinki: "))
for i in range(1,a+1):
    for x in range(1,i):
        print("*", end=" ")
    print()


def silnia(n):
    if n > 1:
        return n*silnia(n-1)
    return 1
print(silnia(4))

qa=randint(1,10)
b=0
while a!=b:
    b = int(input("Podaj b: "))
    if b>a:
        print("podana liczba jest za duża")
    elif b<a:
        print("podana liczba jest za mała")
    else:
        print("brawo zgadłeś")
lista=[]
y=6
for i in range(0,6):
    y=y-1
    print(i,y)
for i in range(1,6):
    a=randint(2,9)
    lista.append(a)

print(lista)
print(len(lista))
print(lista[-1])

lsita =[23,45,1,2,8,3,11,19]
def bubble(lsita):
    for i in range(lsita):
        for x in range(lsita):
            if lsita[x] > lsita[x+1]:
                lsita[x+1],lsita[x]=lsita[x],lsita[x+1]
    return lsita
print(bubble(lsita))

szyfrogram = []
for i in szyfrogram:
    szyfrogram

def pierwsza(x: int) -> bool:
    if x<=1:
        return False
    for i in range(2,int(x**0.5) +1):
        if x%i==0:
            return True
    return False

#sitooooooooootreresa
tab=[]
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


    # rozklad
    def czynniki_pierwsze(n: int) -> list:
        k = 2
        tab = []
        while n > 1:
            while n % k == 0:
                tab.append(k)
                n //= k
            k += 1
        return tab
