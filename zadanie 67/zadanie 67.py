#zadanie 1
def Fb(x):
    a=0
    b=1
    for i in range(x-1):
        a,b=b,a+b
    return b
print(Fb(1))

with open("wyniki67.txt","w") as file:
    file.write("zadanie 1" +"\n")
    file.write(str(Fb(10))+"\n")
    file.write(str(Fb(20))+"\n"+str(Fb(30))+"\n"+str(Fb(40))+"\n")
#zadanie 2
with open("wyniki67.txt","a") as file:
    file.write("zadanie 2"+"\n")

def pierwsza(x):
    if x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
lista_fb=[]
for i in range(40):
    lista_fb.append(Fb(i))
for i in lista_fb:
    if pierwsza(int(i))==True:
        with open("wyniki67.txt","a") as file:
            file.write(str(i) + "\n")
#zadanie 3
a="11110001010000111010100010"

with open("wyniki67.txt","a") as file:
    for i in range(40):
        file.write(str(bin(Fb(i)))[2:]+"\n")
    file.write("*2"+"\n")
    for i in range(40):
        for j in range(len(a)-len((str(bin(Fb(i)))[2:]))):
            file.write("0")
        file.write(str(bin(Fb(i)))[2:]+"\n")
#zadanie 4
def ile_1(x):
    a=0
    for i in x:
        if int(i)==1:
            a=a+1
    return a
with open("wyniki67.txt","a") as file:
    file.write("zadanie4"+"\n")
for i in range(40):
    if ile_1(str(bin(Fb(i)))[2:]) == 6:
        with open("wyniki67.txt","a") as file:
            file.write(str(bin(Fb(i)))[2:]+"\n")





