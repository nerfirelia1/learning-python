liczby_8=[]
liczby_10=[]
liczby_88=[]
with open("liczby1.txt") as file:
    for i in file:
        liczby_88.append(int(i))

with open("liczby1.txt") as file:
    for i in file:
        liczby_8.append(int(i,8))

with open("liczby2.txt") as file:
    for i in file:
        liczby_10.append(int(i))

#zadanie 1
max=0
min=1000000
for i in liczby_88:
    if i>max:
        max=i
    if i<min:
        min=i
with open("wyniki62.txt","w") as file:
    file.write("zadanie 1"+"\n")
    file.write(str(min)+"\n")
    file.write(str(max)+"\n")

#zadanie 2
dl_ciag=1
a=liczby_10[0]
a_maxciagu=liczby_10[0]
max_dlciag=1
for i in range(len(liczby_10)-1):
    if liczby_10[i] <= liczby_10[i+1]:
        dl_ciag+=1
    elif dl_ciag > max_dlciag:
        max_dlciag=dl_ciag
        dl_ciag=1
        a_maxciagu=a
        a=liczby_10[i+1]
    else:
        dl_ciag=1
        a=liczby_10[i+1]

with open("wyniki62.txt","a") as file:
    file.write("zadanie 2" +"\n")
    file.write(str(a_maxciagu)+"\n")
    file.write(str(max_dlciag)+"\n")

#zadanie 3
liczby_wierszy=0
liczby_wierszy_b=0
for i in range(1000):
    if liczby_10[i]==liczby_8[i]:
        liczby_wierszy+=1
for j in range(1000):
    if liczby_8[j]>liczby_10[j]:
        liczby_wierszy_b+=1

with open("wyniki62.txt","a") as file:
    file.write("zadanie 3"+"\n")
    file.write(str(liczby_wierszy)+"\n")
    file.write(str(liczby_wierszy_b)+"\n")

#zadanie 4

def z_dzies(liczba,system):
    wynik=""
    while liczba>0:
        a=liczba%system
        wynik=str(a)+wynik
        liczba=liczba//system
    return wynik
liczby=[]
ile_6=0
for i in liczby_10:
    liczby=str(i)
    for j in range(len(str(liczby))):
        if liczby[j]=="6":
            ile_6+=1
with open("wyniki62.txt","a") as file:
    file.write("zadanie 4" + "\n")
    file.write(str(ile_6)+"\n")
liczby_osemk=[]
for i in liczby_10:
    liczby_osemk.append(z_dzies(int(i),8))
liczby1=[]
ile_6_2=0
for i in liczby_osemk:
    liczby1=i
    for j in range(len((liczby1))):
        if liczby1[j]=="6":
            ile_6_2+=1
with open("wyniki62.txt","a")as file:
    file.write(str(ile_6_2) + "\n")
