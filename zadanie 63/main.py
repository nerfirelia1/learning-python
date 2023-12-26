ciagi=[]
with open("ciagi (1).txt") as file:
    for i in file:
        ciagi.append(i.strip())
#zadanie 1
ciagi_1=[]
for i in ciagi:
    w1=i[:len(i)//2]
    w2=i[len(i)//2:]
    if w1==w2:
        ciagi_1.append(i)
with open("wyniki63.txt","w")as file:
    file.write("zadanie 1" +"\n")
    for i in ciagi_1:
        file.write(str(i)+"\n")

#zadanie 2
ciagi_2=[]
ile_ciag=0
ile_1=0
for i in ciagi:
    ciagi_2=i
    for j in range(len(ciagi_2)-1):
        if ciagi_2[j]=="1" and ciagi_2[j+1]==ciagi_2[j]:
            break
    else:
        ile_ciag+=1
#print(ile_ciag)

with open("wyniki63.txt","a") as file:
    file.write("zadanie 2" +"\n")
    file.write(str(ile_ciag) + "\n")

#zadanie 3

def pierwsza(x):
    x=int(x)
    if x==1:
        return False
    if x==2:
        return True
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
def na_dzies(x):
    wynik=0
    x=str(x)
    dl=len(x)-1
    for i in range(dl):
        wynik+=int(x[i])*2**dl
        dl=dl-1
    return wynik
pierwsze=[]
ciagi_polpierwsze=0
max_polpierwsza=0
min_polpierwsza=10000
for i in ciagi:
    pierwsze=[]
    x=na_dzies(i)
    for j in range(2,na_dzies(i)//2+1):
        if na_dzies(i)%j==0:
            if pierwsza(j)==True:
                x=x//j
                pierwsze.append(j)
                if len(pierwsze)>2:
                    break
    if x>1:
        continue
    #print(i)
    if len(pierwsze)==2:
       # print(na_dzies(i))
        if max_polpierwsza<pierwsze[0]*pierwsze[1]:
            max_polpierwsza=pierwsze[0]*pierwsze[1]
        if min_polpierwsza>pierwsze[0]*pierwsze[1]:
            min_polpierwsza=pierwsze[0]*pierwsze[1]
        ciagi_polpierwsze+=1

print(ciagi_polpierwsze)
print(max_polpierwsza)
print(min_polpierwsza)

def pierwsza1(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def na_dzies1(x):
    return int(x, 2)  # Uproszczona konwersja z binarnego na dziesiętny





"""for i in ciagi:
    x = na_dzies(i)
    if pierwsza(x):
        continue  # Pomijamy liczby pierwsze
    for j in range(2, int(x**0.5) + 1):
        if x % j == 0 and pierwsza(j) and pierwsza(x // j):
            ciagi_polpierwsze += 1
            if x > max_polpierwsza:
                max_polpierwsza = x
            if x < min_polpierwsza:
                min_polpierwsza = x
            break  # Znaleziono liczby półpierwsze, nie ma potrzeby dalszego sprawdzania

# Wyniki
print("Ciągów półpierwszych:", ciagi_polpierwsze)
print("Największa liczba półpierwsza:", max_polpierwsza)
print("Najmniejsza liczba półpierwsza:", min_polpierwsza)
"""

def pierwsza(x):
    x=int(x)
    if x==1:
        return False
    if x==2:
        return True
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
def na_dzies(x):
    wynik=0
    x=str(x)
    dl=len(x)-1
    for i in range(dl):
        wynik+=int(x[i])*2**dl
        dl=dl-1
    return wynik
pierwsze=[]
ciagi_polpierwsze=0
max_polpierwsza=0
min_polpierwsza=10000
for i in ciagi:
    pierwsze=[]
    x=na_dzies(i)
    for j in range(2,na_dzies(i)//2 +1):
        if na_dzies(i)%j==0:
            if pierwsza(j)==True:
                x=x//j
                pierwsze.append(j)
                if len(pierwsze)>2:
                    break
    if x>1:
        continue
    print(i)
    if len(pierwsze)==2:
        print(na_dzies(i))
        if max_polpierwsza<pierwsze[0]*pierwsze[1]:
            max_polpierwsza=pierwsze[0]*pierwsze[1]
        if min_polpierwsza>pierwsze[0]*pierwsze[1]:
            min_polpierwsza=pierwsze[0]*pierwsze[1]
        ciagi_polpierwsze+=1







