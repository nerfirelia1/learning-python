
tekst=[]
with open("tekst.txt") as file:
    for i in file:
        slowa=i.split()
        for n in slowa:
            tekst.append(n.strip())
#zadanie 1
def dwie_litery(x):
        for i in range(len(x)-1):
            if x[i]==x[i+1]:
                return True
        return False
slowa_1=0
for i in tekst:
    if dwie_litery(i)==True:
        slowa_1+=1
with open("wyniki73.txt","w") as file:
    file.write("zadanie 1" +"\n")
    file.write(str(slowa_1)+"\n")

#zadanie 2
lista_liter=[0]*26
for i in tekst:
    for j in i:
        z=ord(j)
        lista_liter[z-65]+=1
suma=sum(lista_liter)
with open("wyniki73.txt","a") as file:
    file.write("zadanie 2" +"\n")
    file.write(str(suma)+"\n")
    for i in range(26):
        file.write(chr(65+i)+" "+ str(lista_liter[i])+" "+str(round(lista_liter[i]/suma*100,2))+"\n")


#zadanie 3
samogloski=["A","E","I","O","U","Y"]
podslowa=0
podslowa_1=[]
max_1=0
for i in tekst:
    a=0
    max_0=0
    for j in i:
        if j not in samogloski:
            a+=1
            if a>max_0:
                max_0=a
        else:
            a=0
    if max_0 >= max_1:
        if max_0>max_1:
            podslowa_1=[]
            podslowa=0
            max_1 = max_0
        podslowa+=1
        podslowa_1.append(i)

with open("wyniki73.txt","a") as file:
    file.write("zadanie 3"+"\n")
    file.write(str(max_1)+"\n")
for i in podslowa_1:
    with open("wyniki73.txt","a") as file:
        file.write(i + " ")





