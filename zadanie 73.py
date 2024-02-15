#zadanie 1

y=19*61/125
y_1=-32-2/3
def f(x):
    return x**4/500 - x**2/200 - 3/250
def f_1(x):
    return -x**3/30 +x/20 +1/6

def całkowanie_prostok(a,b,n):
    suma=0
    x=(b-a)/n
    h=x/2
    for i in range(n):
        z=a+h+i*x
        suma+=f(z)*x
    return suma

w1=całkowanie_prostok(2,10,10000)


def całkowanie_prostok_2(a,b,n):
    suma=0
    x=(b-a)/n
    h=x/2
    for i in range(n):
        z=a+i*x+h
        suma+=f_1(z)*x
    return suma

print(abs(całkowanie_prostok_2(2,10,10000)))
w2=abs(całkowanie_prostok_2(2,10,10000))
w3=round(w1+w2,3)
print(w3)
with open("wyniki70.txt","w") as file:
    file.write("zadanie 1" + "\n")
    file.write(str(w3)+"\n")

#zadanie 2
suma=0
x=2
f2=0
g2=0
h=8/100000
for i in range(1,100001):
    a=(h*h+(f(x+i*h)-f(x+(i-1)*h))**2)**0.5
    b=(h*h+(f_1(x+i*h)-f_1(x+(i-1)*h))**2)**0.5
    f2+=a
    g2+=b
wynik2=f2+g2+y-y_1+16
print(g2,f2)
print(wynik2)

#zadanie 3
def całkowanie_prostok_2():
    suma=0
    x=0.25
    i=9.75
    while i>=2:
        suma+=int(f(i)-f_1(i))
        i-=0.25

    return suma
print(całkowanie_prostok_2())

with open("wyniki70.txt","a") as file:
    file.write("zadanie 3" + "\n")
    file.write(str(całkowanie_prostok_2()))
