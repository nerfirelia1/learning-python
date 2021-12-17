""""
def hello(name):
    print(f"Hello {name}")


name = "John"

hello("Jasiu")

print("Hello {}".format(name))

print("Hello " + name)


def awesome_func(x, y):
    return x**y


print(awesome_func(2, 4))

#------------------------------------------------cwiczenia z petlami ------------------------------

x=0
for x in range(0,4):
    print(x)
#1
    def wyswietl (a,z,e):
        a -= 2
        for a in range (a,z,e):
            a+=e
            print(a)


    wyswietl(1,2,3)

  #2

x = 0
for i in range (5):
    x = x+6
    print(x)

    #3
    y=0
    for i in range (5):
        y = y+i
        print(y)

    #5
    for z in range (52,57):
        z+=1
        print(z)

    #6
    for a in range (7):
        a+=1
        if a == 5:

            print("znalazłem 5!")
            continue


        print(a)

    #7
    for i in range (3):
        i =i+1
        print(i,"a")
        print(i , "b")
        print(i , "c")
    #8
    a = list(range(1,9))
    print(a)

    #9
    for i in a:
        if i == 5:
            break
        print(i)
    #10

    i =4
    while i < 19:
        i = i+2
        print(i)

    #11
lista = ["AA", "BBB","CCCC","DDDDD"]
for k in lista:
        print(k)
else:
    print("lista się skończyła",)

#12

for v in range(1,20):
    if v % 3 == 0:
        print(v)

#13
g=1
while g < 22:

    print(g)
    g=g+5
#14
x =10
while x >-1:
    print(x)
    x= x-1
h= 0
def licz(x,y):
    while (x<y):
        print(x)
        x = x+1

licz(4,9)


#15
# x = godziny
# y = minuty
# z = sekundy

z = int(input("Podaj sekundy: "))
x = z//3600
r = z%3600
y = r//60
r1 = z%60
print("godzin: ", x)
print("minut: ", y)
print("sekund: ", r1)
"""































