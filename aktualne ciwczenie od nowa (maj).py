n=[2,5,23,2,1,0]
def bubble_sort(n:list)-> list:
    for i in range(len(n)):
        for j in range(len(n)-i-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    return n

lista=[1,3,5,6,45,0,3]
def selection_sort(lista:list)-> list:
    for i in range(len(lista)):
        mini=i
        for j in range(i+1,len(lista)):
            if lista[mini]>lista[j]:
                lista[mini],lista[j]=lista[j],lista[mini]
    return lista

def rozkladnapierwszeczynniki(x):
    wspolczynniki=[]
    i=2
    while x>1:
        while x%i==0:
            wspolczynniki+=[i]
            x=x//i
        i=i+1
    return wspolczynniki


def spawdzpierwsza(x) -> bool:
    if x==2:
        return True
    for i in range(2,x):
        if x%i==0:
            return False
    return True

tab = []
for i in range(101):
    tab.append(True)
print(tab)


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
        if tab[i]== True:
            print(i, "jest liczba pierwsza")
    return tab
sito(10,100,tab)

def pierwsza(x:int) -> bool:
    if x==1 or x==2:
        return True
    for i in range(2,x):
        if x%i==0:
            return False
    return True
print(pierwsza(13))

def doskonała(x:int) -> bool:
    suma=0
    for i in range(1,x):
        if x%i==0:
            suma=suma+i
    if suma==x:
        return True
    return False
print(doskonała(6))
print(doskonała(28))
print(doskonała(497))

def silinia(x):
    silinia1=1
    for i in range(1,x+1):
        silinia1=silinia1*i
    return silinia1
print(silinia(5))
print(silinia(3))

def silniareku(n):
    if n > 1:
        return n*silniareku(n-1)
    return 1
print(silniareku(4))

def sumacyfrliczby(x:int)->int:
    suma=0
    for i in range(1,x+1):
        suma=suma+i
    return suma

def sumacyfrliczbyreku(x:int)-> int:
    if x>0:
        return x+sumacyfrliczbyreku(x-1)
    return 0
print(sumacyfrliczbyreku(10))

def nwd_iter(a: int, b: int) -> int:
    while b > 0:
        a, b = b, a % b
    return a
print(nwd_iter(20,8))

#Spoko stronka z algorytmami na maturke + wyjasnienia pojec - https://maturka.it/algorytmy/

def NWW(a:int, b: int) -> int:
    return a*b//(nwd_iter(a,b))

NWW(14,28)