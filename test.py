#zad1

def suma_cyfr_pierwsza(x):
    suma=0
    x=str(x)
    for i in x:
        suma+=int(i)
    for i in range(2,suma):
        if suma%i==0:
            return False
    return True
lista=[]
for i in range(500):
    lista.append(True)

def zad1(a,b,lista):
    for i in range(2,b):
        if lista[i]==True:
            j=i*2
            while j<=b:
                lista[j]=False
                j=j+i
    for x in range(a,b+1):
        if lista[x]==True and suma_cyfr_pierwsza(x)==True:
            print(x,"jest liczba pierwsza")

    return 1
zad1(2,100,lista)

zad1(10,50,lista)

zad1(50,100,lista)

#zad 2

def dzielniki(x):
    dzielniki_1=[]
    a=x
    for i in range(x):
        if a==1:
            return dzielniki_1
        if x%a==0:
            dzielniki_1.append(a)
        a=a-1
    return dzielniki_1
print(dzielniki(50))


def zad2(lista_liczb):
    a=min(lista_liczb)
    y=-1
    for i in range(len(dzielniki(a))):
        y=y+1
        b=0
        x=dzielniki(a)[y]
        for j in lista_liczb:
            if x in dzielniki(j):
                b=b+1
        if b==len(lista_liczb):
            return x
print(zad2([60,48,36]))
print(zad2([100,80,120]))
print(zad2([20,30,18]))

#zad3

def zad4_iter(x):
    lista=[]
    a=0
    b=1
    c=1
    for i in range(x):
        lista.append(a)
        if len(lista)==x:
            return lista
        lista.append(b)
        if len(lista)==x:
            return lista
        lista.append(c)
        if len(lista)==x:
            return lista
        a=a+b+c
        b=a+b+c
        c=a+b+c
    return lista
print(zad4_iter(10))
print(zad4_iter(7))
print(zad4_iter(13))


def zad5(x,y):
    if len(x)>=len(y):
        for i in x:
            if i not in y:
                return False
        for i in y:
            if i not in x:
                return False
            continue
    if len(y)>len(x):
        for i in y:
            if i not in x:
                return False
        for i in x:
            if i not in y:
                return False
            continue
    return True
print(zad5("aabbccdd","dcba"))
print(zad5("abcdddee","abcd"))
print(zad5("accbterhy","accbterhyw"))
print(zad5("oko","oko"))






