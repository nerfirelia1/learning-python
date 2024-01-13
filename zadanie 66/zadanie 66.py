lista1=[]
lista2=[]
lista3=[]
with open("trojki.txt")as file:
    for i in file:
        a,b,c=i.split()
        lista1.append(int(a))
        lista2.append(int(b))
        lista3.append(int(c))

#zadanie 1
def suma_cyfr(x):
    x=str(x)
    suma=0
    for i in range(len(x)):
        suma=suma+int(x[i])
    return suma

trojki=[]
for i in range(1000):
    if suma_cyfr(lista1[i]) + suma_cyfr(lista2[i])==lista3[i]:
        trojki.append(i)
with open("wyniki66.txt","w") as file:
    file.write("zadanie 1" + "\n")
    for i in trojki:
        file.write(str(lista1[i])+" "+str(lista2[i])+" "+str(lista3[i]))
        file.write("\n")

#zadanie 2

def pierwsza(x):
    if x==2:
        return True
    for i in range(2,x):
        if x%i==0:
            return False
    return True
with open("wyniki66.txt","a") as file:
    file.write("zadanie 2" + "\n")
for i in range(1000):
    if pierwsza(lista1[i])==True and pierwsza(lista2[i])==True and lista1[i] * lista2[i]==lista3[i]:
        with open("wyniki66.txt","a") as file:
            file.write(str(lista1[i]) + " "+str(lista2[i]) + " " + str(lista3[i]) +"\n")

#zadanie 3
with open("wyniki66.txt","a") as file:
    file.write("zadanie 3" + "\n")
def warunek_prost(a,b,c):
    if b**2 + c**2 == a**2:
        return True
    if b**2 + a**2==c**2:
        return True
    if a**2 + c**2 == b**2:
        return True
    return False
for i in range(999):
    if warunek_prost(lista1[i],lista2[i],lista3[i])==True and warunek_prost(lista1[i+1],lista2[i+1],lista3[i+1]) == True:
        with open("wyniki66.txt","a") as file:
            file.write(str(lista1[i]) + " "+str(lista2[i]) + " "+str(lista3[i])+"\n"+str(lista1[i+1])+" "+str(lista2[i+1]) +" "+str(lista3[i+1])+"\n"+"\n" )

#zadanie 4

with open("wyniki66.txt","a")as file:
    file.write("zadanie 4" + "\n")
ile_tr=0
max_ciag=1
lista=[]
def warunek_tr(a,b,c):
    if a+b >c and b+c >a and a+c>b:
        return True
    return False
for i in range(1000):
    if warunek_tr(lista1[i],lista2[i],lista3[i]) == True:
        ile_tr+=1
        lista.append("a")
    else:
        lista.append("b")
ciag=1


for i in range(len(lista)-1):
    if lista[i]=="a" and lista[i+1]=="a":
        ciag+=1
    else:
        ciag=1
    if ciag>max_ciag:
        max_ciag=ciag
with open("wyniki66.txt","a") as file:
    file.write(str(ile_tr) + " " + str(max_ciag) + "\n")


b,c=a.split()
print(b,c)
