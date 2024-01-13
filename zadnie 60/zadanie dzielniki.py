#zadanie 1

liczby=[]
with open("liczby2.txt") as file:
    for line in file:
        liczby.append(int(line))
ile_liczb=0
liczby1=[]
for i in liczby:
    if i<1000:
        liczby1.append(i)
        ile_liczb+=1
a=liczby1[-1]
b=liczby1[-2]
with open("wyniki60.txt","w") as file:
    file.write("zadanie 1"+"\n")
    file.write(str(ile_liczb)+"\n")
    file.write(str(a)+"\n")
    file.write(str(b)+"\n")

#zadanie 3

def NWD(a,b):
    if a%b==0:
        return b
    return NWD(b,a%b)
max3=-1
for i in liczby:
    for j in liczby:
        if i!=j and NWD(i,j)>1:
            break
    else:
        if i>max3:
            max3=i
with open("wyniki60.txt","a") as file:
    file.write("zadanie 3"+"\n")
    file.write(str(max3)+"\n")


"""i=1
while i<10:
    print(i)
    i=i+1
    if i==6:
        break
else:
    print(2)
"""
#zadanie 2

with open("wyniki60.txt","a") as file:
    file.write("zadanie 2" + "\n")

for i in liczby:
    ile2=2
    lista=[1,i]
    for j in range(2,int(i**0.5 +1)):
        if i%j==0:
            ile2+=2
            lista.append(j)
            lista.append(i//j)
            if i==j*j:
                ile2=ile2-1
                lista.pop()
    if ile2==18:
        lista.sort()
        with open("wyniki60.txt","a")as file:
            file.write(str(i)+"\n")
            for line in lista:
                file.write(str(line)+" ")
            file.write("\n")




#with open("wyniki60_2_cw","w") as file:




liczby=[]
with open("liczby2.txt") as file:
    for line in file:
        liczby.append(line)
ile_1000=0
mniejsze100=[]
for i in liczby:
    if int(i)<1000:
        ile_1000+=1
        mniejsze100.append(i)
with open("wyniki60_2_cw","w") as file:
    file.write("zadanie 1"+"\n")
    file.write(str(mniejsze100[-1])+ " " +str(mniejsze100[-2]) + "\n")
    file.write(str(ile_1000)+"\n")

with open("wyniki60_2_cw","a") as file:
    file.write("zadanie 2"+"\n")
def ile_dzielnych(x):
    suma=0
    for i in range(1,x+1):
        if x%i==0:
            suma+=1
    return suma
liczby_18=[]
for i in liczby:
    dzielniki=[]
    if ile_dzielnych(int(i))==18:
        for j in range(1, int(i) + 1):
            if int(i) % j == 0:
                dzielniki.append(j)
        with open("wyniki60_2_cw","a") as file:
            file.write(str(i)+" "+str(dzielniki)+"\n")

#zadanie 3
def nwd(a,b):
    if a%b==0:
        return b
    return nwd(b,a%b)
max=1
for i in liczby:
    liczba = int(i)
    for j in liczby:
        if liczba==int(j):
            continue
        if nwd(liczba,int(j))==1:
            if liczba>max:
                max=liczba
print(max)

#zapytanie!!!!
def NWD(a,b):
    if a%b==0:
        return b
    return NWD(b,a%b)
max3=-1
for i in liczby:
    for j in liczby:
        if i!=j and NWD(int(i),int(j))>1:
            break
    else:
        if int(i)>max3:
            max3=int(i)
print(max3)
































