liczniki=[]
mianowniki=[]
with open("dane_ulamki.txt") as file:
    for line in file:
        a,b=line.split()
        liczniki.append(int(a))
        mianowniki.append(int(b))
#zadanie 1
licz=0
min=100000
min_mianownik=10000

for i in range(len(liczniki)):
    if liczniki[i]/mianowniki[i]<min:
        min=liczniki[i]/mianowniki[i]
        licz=liczniki[i]
        min_mianownik=mianowniki[i]
    elif liczniki[i]/mianowniki[i]==min:
        if mianowniki[i]<min_mianownik:
            min=liczniki[i]/mianowniki[i]
            min_mianownik=mianowniki[i]
            licz=liczniki[i]
with open("wyniki65.txt","w") as file:
    file.write("Zadanie 1" + "\n")
    file.write(str(licz)+ " "+str(min_mianownik) + "\n")

#zadanie 2
nieskr=0
def NWD(a,b):
    if a%b==0:
        return b
    return NWD(b,a%b)
for i in range(len(liczniki)):
    if NWD(liczniki[i],mianowniki[i])==1:
        nieskr+=1

with open("wyniki65.txt","a") as file:
    file.write("zadanie 2" + "\n")
    file.write(str(nieskr)+"\n")

#zadanie 3

def skroc(a,b):
    x=a//NWD(a,b)
    return x
liczniki_nieskr=[]
for i in range(len(liczniki)):
    liczniki_nieskr.append(skroc(liczniki[i],mianowniki[i]))
suma=0
for i in liczniki_nieskr:
    suma=suma+i
with open("wyniki65.txt","a") as file:
    file.write("zadanie 3"+"\n")
    file.write(str(suma)+"\n")

#zadanie 4

b=2**2 * 3**2 * 5**2 * 7**2 * 13
suma_pocz=0
for i in range(len(liczniki)):
    suma_pocz+=b*liczniki[i]/mianowniki[i]
suma=suma_pocz/b

with open("wyniki65.txt","a") as file:
    file.write("zadanie 4" + "\n")
    file.write(str(round(suma,2)) +" " +str(suma_pocz))



