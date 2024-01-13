def spawdzpierwsza(x) -> bool:
    if x==2:
        return True
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def rozkladnapierwszeczynniki(x):
    wspolczynniki=[]
    i=2
    while x>1:
        while x%i==0:
            wspolczynniki+=[i]
            x=x//i
        i=i+1
    return wspolczynniki
print(rozkladnapierwszeczynniki(100))


tab = []
for i in range(360):
    tab.append(True)

def sito(a: int, b: int, tab: list) -> int:
    for i in range(2, int(b ** 0.5) + 1):
        if tab[i] == True:
            j = i * 2
            while j <= b:
                tab[j] = False
                j += i
    for i in range(a, b + 1):
        if tab[i]== True:
            print(tab[i])
            print(i, "jest liczba pierwsza")
    return "no siemea"
sito(20,120,tab)
def pierwsza(x:int) -> bool:
    if x==1 or x==2:
        return True
    for i in range(2,x):
        if x%i==0:
            return False
    return True
print(pierwsza(179))

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
print(silinia(6))
print(silinia(3))

def silniareku(n):
    if n > 1:
        return n*silniareku(n-1)
    return 1
print(silniareku(1))

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
print(nwd_iter(8,20))

#Spoko stronka z algorytmami na maturke + wyjasnienia pojec - https://maturka.it/algorytmy/

def NWW(a:int, b: int) -> int:
    return a*b//nwd_iter(a,b)
print(NWW(14,28))

def fib_i(n):
    if n == 0: return 0
    elif n == 1: return 1
    p, w = 0, 1
    for i in range(n-1):
        p, w = w, p+w
        print(p,w)
    return w
print(fib_i(10))

def anagram(A:str,B:str) -> str:
    A=list(A)
    B=list(B)
    for n in range(len(A)):
        for n in range(len(A)-1-n):
            if A[n]>A[n+1]:
                A[n],A[n+1]=A[n+1],A[n]
    for m in range(len(B)):
        for m in range(len(B)-1-m):
            if B[m]>B[m+1]:
                B[m],B[m+1]=B[m+1],B[m] 
    print(A)
    print(B)
    if A==B:
        return "tak"
    return "nie"
print(anagram("matuRa","traums"))
a=[4,67676,3434,7,76,7,6]
print(len(a))

def insertion(lista:list)-> list:
    for i in range(1,len(lista)):
        liczba = lista[i]
        while i>0 and lista[i-1] > liczba:
            lista[i] = lista[i-1]
            i=i-1
        lista[i] = liczba
    return lista

print(insertion([2,7,6,2,6,9076,0,1]))
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

def reszta_zachłannie(x,y):
    lista = []
    i=0
    while x>0:
        while y[i]<=x:
            lista.append(y[i])
            x-=y[i]
        i=i+1
    return lista
lista1=[500,200,100,50,20,10,5,2,1]

def znajdz_max_min(list:list) -> int:
    x=list[0]
    a=list[0]
    for i in list:
        if i>x:
            x=i
        elif i<a:
            a=i
    return a,x
print(znajdz_max_min([-348,6,4,5,7676,1,76,121]))

def sprawdzczytr(A,B,C):
    if A <=0 or B<=0 or C <=0:
        return False
    if A+B > C and A+C > B and B+C > A:
        return True
    return False
print(sprawdzczytr(7,1,6))


def schHornera(n,T,C):
    lista=[]
    lista.append(T[0])
    wynik=T[0]
    for i in range(1,n+1):
        wynik = wynik * C +T[i]
        lista.append(wynik)
    return lista
print(schHornera(3,[1,-3,5],3))

def f(x):
    return x**3*2

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
print(bisekcja(-3,7))



def dl(x1,y1,x2,y2):
    dl1=(((x2-x1)**2) + ((y2-y1)**2))
    return (dl1**0.5)
def czywsrodkutrojaktapunkt(Ax,Ay,Bx,By,Cx,Cy,Dx,Dy):
    AB=dl(Ax,Ay,Bx,By)
    AC=dl(Ax,Ay,Cx,Cy)
    BC=dl(Bx,By,Cx,Cy)
    ad=dl(Ax,Ay,Dx,Dy)
    bd=dl(Bx,By,Dx,Dy)
    cd=dl(Cx,Cy,Dx,Dy)
    i=(AB+AC+BC)/2
    p=(i*(i-AB)*(i-BC)*(i-AC))**0.5
    j=(AB+ad+bd)/2
    k=(AC+cd+ad)/2
    l=(BC+cd+bd)/2
    p2=((j*(j-ad)*(j-bd)*(j-AB)))**0.5 + (k*(k-AC)*(k-cd)*(k-ad))**0.5 + ((l*(l-BC)*(l-cd)*(l-bd)))**0.5
    if p==p2:
        return "Tak"
    return "Nie"

def potegowanieszybkie(x,y):
    c=x
    wynik =1
    while y>0:
        if y%2==1:
            wynik=wynik*x
        x=x*x
        y=y//2
    return wynik
print(potegowanieszybkie(4,5))

def wyszukiwanie_binarne(arr,x):
    l=0
    r=len(arr) -1
    mid = (l+r) // 2
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            r=r-1
        else:
            l=l+1
print(wyszukiwanie_binarne([1,2,3,4,6,7],5))

def binary_selection_recurrent(list,target,l,r):
    if l<=r:
        mid=(l+r)//2
    if list[mid]==target:
        return mid
    elif list[mid]>target:
        return binary_selection_recurrent(list,target,l,mid-1)
    elif list[mid]<target:
        return binary_selection_recurrent(list,target,mid+1,r)

def wspolczynniki(x:int):
    lista=[]
    for i in range(2,x):
        while x%i==0:
            lista.append(i)
            x=x//i
    return lista
print(wspolczynniki(25))


#ASCII
print(ord('A'))
print(chr(65))

def cezar(slowo:str, klucz:int)->str:
    a=list(slowo)
    wynik=""
    for i in a:
        if ord(i) >=65 and ord(i)<=90:
            wynik=wynik+chr((ord(i)+klucz-65)%26 +65)
        elif ord(i)>=97 and ord(i)<=122:
            wynik=wynik+ chr((ord(i)+klucz-97)%26 +97)
        else:
            wynik+=i
    return wynik

print(cezar("sIemA",3))

def conversion_on_tens(liczba,system):
    wynik=0
    liczba = str(liczba)
    dl=len(liczba)-1
    for i in liczba:
        wynik+=(system**dl)*int(i)
        dl=dl-1
        print(wynik)
    return wynik

def fib_rek(n):
    """
        Funkcja zwraca n-ty wyraz ciągu Fibonacciego.
        Wersja rekurencyjna.
    """
    if n < 1:
        return 0
    if n < 2:
        return 1
    print(n)
    return fib_rek(n - 1) + fib_rek(n - 2)

