def wyszukiwanie_binarne(lista,l,r,szuk):
    if lista[(l+r)//2] == szuk:
        return (l+r)//2
    if lista[(l + r) // 2] > szuk:
        return wyszukiwanie_binarne(lista,l,(l+r)//2 -1,szuk)
    else:
        return wyszukiwanie_binarne(lista,(l+r)//2 +1,r,szuk)
print(wyszukiwanie_binarne([1,2,3,4,5,7],0,len([1,2,3,4,5,7]),5))

def potegowanie_szybkie(x,y):
    wynik =1
    while y>0:
        if y%2==1:
            wynik=wynik*x
        x=x*x
        y=y//2
    return wynik
print(potegowanie_szybkie(3,4))

def czy_anagramy(ciag1, ciag2):
    # Sprawdź długość ciągów
    if len(ciag1) != len(ciag2):
        return False

    # Zainicjuj tablice liczników
    liczniki1 = [0] * 4000  # Załóżmy, że używamy ASCII, można dostosować dla innych zestawów znaków
    liczniki2 = [0] * 4000
    print(liczniki1,liczniki2)

    # Zlicz wystąpienia znaków w obu ciągach
    for char in ciag1:
        liczniki1[ord(char)] += 1

    for char in ciag2:
        liczniki2[ord(char)] += 1

    # Porównaj tablice liczników
    return liczniki1 == liczniki2

# Przykłady użycia
ciag1 = "listen"
ciag2 = "silent"
wynik = czy_anagramy(ciag1, ciag2)

def sortuj(x):
    for i in range(len(x)):
        mini_indeks=i
        for j in range(i+1,len(x)):
            if x[mini_indeks]>x[j]:
                x[mini_indeks],x[j]=x[j],x[mini_indeks]
    return x
print(sortuj([2,6,45,31,2,0,34]))

def Anagram(z,y):
    z=list(z)
    y=list(y)
    if sortuj(z)==sortuj(y):
        return True
    return False

def z_dzies(x,system):
    wynik=""
    while x>0:
        wynik=str(x%system) +wynik
        x=x//system
    return wynik

def na_dzies(x,system):
    wynik=0
    x=list(x)
    print(x)
    dl=len(x)-1
    for i in x:
        wynik+=int(i)*system**dl
        dl=dl-1
    return wynik
print(na_dzies("0110",2))




