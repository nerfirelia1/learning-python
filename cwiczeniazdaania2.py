#--------------------FUNKCJE------------------
def silnia(n):
    if n>1:
        return n * silnia(n - 1)
    else:
        return 1
def dodawaniee(a):
    if a >0:
        return a+dodawaniee(a-1)
    else:
        return a
print(dodawaniee(8))
print(dodawaniee(4))
s=0
x=0
a=0
n = int(input("Podaj liczbe: "))

#------------PĘTLE-----------------------
while (n>0):
    x=n%10
    s=s+1
    a=a+x
    n=n//10
print("Liczba składa się z tylu liczb: ",s, "suma liczb wynosi: ", a)



