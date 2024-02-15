hasla=[]
with open("hasla.txt") as file:
    for i in file:
        hasla.append(i.strip())
liczba_hasel=0
for i in hasla:
    if i.isdigit():
        liczba_hasel+=1
with open("wyniki74.txt","w") as file:
    file.write("zadanie 1"+"\n")
    file.write(str(liczba_hasel)+"\n")

#zadanie 2
with open("wyniki74.txt","a") as file:
    file.write("zadanie 2"+"\n")
powtorzenia=[]
for i in range(len(hasla)):
    for j in range(len(hasla)):
        if i==j:
            continue
        if hasla[j]==hasla[i]:
            powtorzenia.append(hasla[j])
powtorzenia=set(powtorzenia)
powtorzenia=list(powtorzenia)
powtorzenia.sort()
"""for i in range(len(powtorzenia)-6):
    if powtorzenia[i+1]==powtorzenia[i]:
        powtorzenia.remove(powtorzenia[i])
"""
with open("wyniki74.txt", "a") as file:
    for i in powtorzenia:
        file.write(i+"\n")

#zadanie 3

def asci_4(x):
    lista_4=[x[0],x[1],x[2],x[3]]
    lista_4.sort()
    return ord(lista_4[0])==ord(lista_4[1])-1 and ord(lista_4[1])==ord(lista_4[2])-1 and ord(lista_4[2])==ord(lista_4[3])-1
ile3=0

for i in hasla:
    for j in range(len(i)-3):
        if asci_4(i[j:j+4]):
            ile3+=1
            break
with open("wyniki74.txt","a") as file:
    file.write("zadanie 3"+"\n")
    file.write(str(ile3)+"\n")

#zadanie 3

def warunek(x):
    a,b,c=0,0,0
    for i in x:
        if i.isdigit():
            a+=1
        if i.islower():
            b+=1
        if i.isupper():
            c+=1
    if a > 0 and b>0 and c>0:
        return True
    return False
hasla_zad3=0
for i in hasla:
    if warunek(i)==True:
        hasla_zad3+=1
with open("wyniki74.txt","a") as file:
    file.write("zadanie 3"+"\n")
    file.write(str(hasla_zad3))



