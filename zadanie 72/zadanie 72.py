"""
def funkcja(x,y):
    if len(x)>len(y):
        return False
    for i in range(len(x)):
        if x[i]!=y[i]:
            return False
    for i in range(len(x)-1,len(y)):
        litery.append(y[i])
    return (litery,True)

print(funkcja("kot","kotara")[1])
suma1=0
for i in range(200):
    if funkcja(napisy_1[i],napisy_2[i])[1]==True:
        suma1+=1
        with open("wyniki72.txt","a") as file:
            file.write(napisy_1[i] + " " +napisy_2[i] + " " +funkcja(napisy_1[i],napisy_2[i])+"\n")
napisy_1=[]
napisy_2=[]
"""
napisy_1=[]
napisy_2=[]
with open("napisy.txt") as file:
    for i in file:
        a,b=i.split()
        napisy_1.append(a)
        napisy_2.append(b)
"""
#zadanie 1
suma=0
napisy_3_len=[]
for i in range(200):
    if len(napisy_1[i])>=len(napisy_2[i])*3 or len(napisy_2[i])>=len(napisy_1[i])*3:
        suma+=1
        napisy_3_len.append(napisy_1[i])
        napisy_3_len.append(napisy_2[i])
with open("wyniki72.txt","w") as file:
    file.write("zadanie1"+"\n")
    file.write(str(suma)+"\n")
    file.write(napisy_3_len[0] + " "+ napisy_3_len[1])

#zadanie 2
litery=[]
def funkcja(x,y):
    if len(x)>len(y):
        return False
    for i in range(len(x)):
        if x[i]!=y[i]:
            return False
    for i in range(len(x)-1,len(y)):
        litery.append(y[i])
    return (litery,True)

print(funkcja("kot","kotara")[1])
print(napisy_1[0],napisy_2[0])
print(funkcja(napisy_1[0],napisy_2[0])[1])

suma1=0
for i in range(200):
    if funkcja(napisy_1[i],napisy_2[i])[1]:
        suma1+=1
        with open("wyniki72.txt","a") as file:
            file.write(napisy_1[i] + " " +napisy_2[i] + " " +funkcja(napisy_1[i],napisy_2[i])+"\n")

"""
#zadanie 3
lista=[1,23,5]
def sprawdz(x,y):
    max=0
    if len(x)>=len(y):
        for i in range(len(y)):
            if y[-i-1]==x[-i-1]:
                max+=1
            else:
                break
    elif len(y)>len(x):
        for i in range(len(x)):
            if x[-i-1]==y[-i-1]:
                max+=1
            else:
                break
    return max
lista_wyrazy=[]
max_1=0
for i in range(200):
    if sprawdz(napisy_1[i],napisy_2[i])>max_1:
        max_1=sprawdz(napisy_1[i],napisy_2[i])
for i in range(200):
    if sprawdz(napisy_1[i],napisy_2[i])==max_1:
        lista_wyrazy.append(napisy_1[i])
        lista_wyrazy.append(napisy_2[i])
print(lista_wyrazy)
with open("wyniki72.txt","a") as file:
    file.write("\n")
    file.write("zadanie 3 " + "\n")
    file.write(str(max_1)+"\n")



