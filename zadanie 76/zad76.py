szyfr1=[]
szyfr2=[]
szyfr3=[]
klucz_1=[]
klucz_2=[]
i=0
with open("szyfr1.txt") as file:
    for line in file:
        i+=1
        if i!=7:
            szyfr1.append(line.strip())
        else:
            k=line.split()
            for kl in k:
                klucz_1.append(int(kl))
#print(klucz_1)
for i in szyfr1:
    x=0
    i=list(i)
    #print(i)
    for j in range(len(i)):
        #print(klucz_1[x])
        i[klucz_1[x]-1],i[j]=i[j],i[klucz_1[x]-1]
        x=x+1
        if x>len(klucz_1):
            x=0
    i="".join(i)
with open("wyniki76.txt","w") as file:
    file.write("zadanie 1"+"\n")
    for i in szyfr1:
        file.write(i+"\n")

#zadanie 2
a=0
with open("szyfr2.txt") as file:
    for line in file:
        if a==1:
            k=line.split()
            for kl in k:
                klucz_2.append(int(kl))
        else:
            a=a+1
            szyfr2.append(line.strip())
s=list(szyfr2)
print(s)
for i in range(len(s)):
    print(s[i])
    z=0
    s[i],s[klucz_2[z]-1]=s[klucz_2[z]-1],s[i]
    z+=1
    if z>=15:
        z=0
    i="".join(i)
with open("wyniki76.txt","a") as file:
    file.write("zadanie 2"+"\n")
    file.write(s+"\n")








