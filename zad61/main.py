#zadanie 1
listaliczb=[]
with open("ciagi.txt") as file:
    for line in file:
        listaliczb.append(line)
ile_arytm=0
maxir=-1
for i in range(1,len(listaliczb),2):
    lista=listaliczb[i].split()
    r=int(lista[1])-int(lista[0])
    for j in range(2,len(lista)):
        if int(lista[j])-int(lista[j-1])!=r:
            break
    else:
        ile_arytm+=1
        if r>maxir:
            maxir=r
with open("wyniki61.txt","w") as file:
    file.write("zadanie 1"+"\n")
    file.write(str(ile_arytm)+"\n")
    file.write(str(maxir)+"\n")

"""print(listaliczb[1])
for i in listaliczb:
    print(i)
"""
#zadanie 2
def szescian(x):
    for i in range(1,101):
        if i**3==x:
            return True
szesciany_max=[]
for i in range(1,len(listaliczb),2):
    lista1=listaliczb[i].split()
    max_sz = -1
    for j in lista1:
        if szescian(int(j))==True:
            max_sz=int(j)
    if max_sz!=-1:
        szesciany_max.append(max_sz)
print(szesciany_max)
listaliczb_1=[]
with open("bledne.txt") as file:
    for i in file:
        listaliczb_1.append(i)

with open("wyniki61.txt","a") as file:
    file.write("zadanie 2" + "\n")
    file.write(str(szesciany_max) + "\n")

#zadanie 3
lista_bledy=[]
for i in range(1,len(listaliczb_1),2):
    list=listaliczb_1[i].split()
    lista_int=[]
    for j in list:
        lista_int.append(int(j))
    r=[]
    for j in range(1,len(lista_int)):
        r.append(lista_int[j]-lista_int[j-1])
    if r[0]!=r[1] and r[2]==r[1]:
        lista_bledy.append(lista_int[0])
        continue
    if r[1]!=r[0] and r[3]==r[2] and r[2]!=r[1]:
        lista_bledy.append(lista_int[1])
        continue
    for j in range(1,len(lista_int)-1):
        if r[0]!=r[j]:
            lista_bledy.append(lista_int[j+1])
            break
with open("wyniki61.txt","a") as file:
    file.write("zadanie 3"+"\n")
    file.write(str(lista_bledy)+ "\n")




ciagi=[]
with open("ciagi.txt") as file:
    for line in file:
        ciagi.append(line)


































