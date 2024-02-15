a0=[]
a1=[]
a2=[]
a3=[]

with open("funkcja.txt") as file:
    for i in file:
        a,b,c,d=i.split()
        a0.append(float(a))
        a1.append(float(b))
        a2.append(float(c))
        a3.append(float(d))

with open("wyniki71.txt","w")as file:
    file.write("zadanie 1" + "\n")
    file.write(str(round(a0[1]+a1[1]*1.5+a2[1]*(1.5)**2+a3[1]*(1.5**3),5))+"\n")

#zadanie 2
wynik_1=0
max_wynik=0
x=0
for j in range(10000):
    wynik_1=a0[4]+(4+j/10000)*a1[4] +a2[4]*(4+j/10000)**2 +a3[4]*(4+j/10000)**3
    if wynik_1>max_wynik:
        x=4+(j/10000)
        max_wynik=wynik_1

with open("wyniki71.txt","a") as file:
    file.write("zadanie 2"+"\n")
    file.write(str(round(max_wynik,5))+"\n")
    file.write(str(round(x,3))+"\n")


def f(x):
    if x<1:
        return a0[0]+a1[0]*x + a2[0]*x**2 + a3[0]*x**3
    elif x<2:
        return a0[1]+a1[1]*x+a2[1]*x**2 + a3[1]*x**3
    elif x<3:
        return a0[2]+a1[2]*x+a2[2]*x**2+a3[2]*x**3
    elif x<4:
        return a0[3]+a1[3]*x+a2[3]*x**2+a3[3]*x**3
    elif x<=5:
        return a0[4]+a1[4]*x+a2[4]*x**2+a3[4]*x**3

def bisekcja(a,b,eps):
    if f(a)*f(b)>0:
        return None
    while b-a>=eps:
        mid=(a+b)/2 
        if f(a) * f(mid)<0:
            b=mid
        elif f(b)*f(mid)<0:
            a=mid
    return mid
x1=bisekcja(0,1,0.00001)
x2=bisekcja(2,3,0.00001)
x3=bisekcja(3,4,0.00001)
x4=bisekcja(4,5,0.00001)
with open("wyniki71.txt","a") as file:
    file.write("zadanie 3"+"\n")
    file.write(str(round(x1,5)) + " "+ str(round(x2,5)) +" "+ str(round(x3,5)) +" "+ str(round(x4,5)) + "\n")







