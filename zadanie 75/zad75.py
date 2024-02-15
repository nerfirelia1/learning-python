slowa=[]
with open("tekst (1).txt") as file:
    for line in file:
        l=line.split()
        for i in l:
            slowa.append(i)
#zadnie 1

with open("wyniki75.txt","w") as file:
    file.write("zadanie 1" + "\n")

for i in slowa:
    if i[0] == "d" and i[-1]=="d":
        with open("wyniki75.txt","a") as file:
            file.write(i+"\n")

def szyfr(slowo,klucz1,klucz2):
    wynik=""
    for i in slowo:
        if ord(i)>=97 and ord(i)<=122:
            wynik+=chr(((ord(i)-97)*klucz1+klucz2)%26+97)
    return wynik
with open("wyniki75.txt","a") as file:
    file.write("zadanie 2"+"\n")

for i in slowa:
    if len(i)>=10:
        with open("wyniki75.txt","a") as file:
            file.write(szyfr(i,5,2)+"\n")

#zadanie 3
jawne=[]
szyfr_afin=[]
with open("probka.txt") as file:
    for line in file:
        a,b=line.split()
        jawne.append(a)
        szyfr_afin.append(b)
for i in range(5):
    for j in range(26):
        for k in range(26):
            if szyfr(szyfr_afin[i],j,k)==jawne[i]:
                with open("wyniki75.txt","a") as file:
                    file.write("klucz deszyfrujacy: " +str(j)+","+str(k) +"\n")
            if szyfr(jawne[i],j,k)==szyfr_afin[i]:
                with open("wyniki75.txt","a") as file:
                    file.write("klucz szyfrujacy: " +str(j)+","+str(k)+"\n")







