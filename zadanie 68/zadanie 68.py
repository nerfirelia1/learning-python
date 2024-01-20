anagramy_1=[]
anagramy_2=[]

with open("dane_napisy.txt") as file:
    for i in file:
        a,b=i.split()
        anagramy_1.append(a)
        anagramy_2.append(b)
#zadanie 1

def anagram(x,y):
    if sorted(x)==sorted(y):
        return True
    return False
def jednolite(x,y):
    a = x[0]
    for i in x:
        if i!=a:
            return False
    if x==y:
        return True
ile=0
for i in range(1000):
    if jednolite(anagramy_1[i],anagramy_2[i])==True:
        if anagram(anagramy_1[i],anagramy_2[i])==True:
            ile+=1
with open("wyniki68.txt","w") as file:
    file.write("zadanie 1"+"\n")
    file.write(str(ile)+"\n")

#zadanie 2
suma=0
for i in range(1000):
    if anagram(anagramy_1[i],anagramy_2[i])==True:
        suma+=1
with open("wyniki68.txt","a") as file:
    file.write("zadanie 2" + "\n")
    file.write(str(suma)+"\n")

#zadanie 3
with open("wyniki68.txt","a") as file:
    file.write("zadanie 3"+"\n")
k=0
lista=[]
lista.extend(anagramy_1)
lista.extend(anagramy_2)
max_k=0
z=0
for j in range(2000):
    a=j
    k=0
    for i in lista:
        if a==z:
            z = z + 1
            continue
        if anagram(lista[a],i)==True:
            k=k+1
    if k>max_k:
        max_k=k
with open("wyniki68.txt","a") as file:
    file.write(str(max_k)+"\n")



