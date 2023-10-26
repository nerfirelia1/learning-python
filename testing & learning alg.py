def reszta_zachłannie(x,y):
    lista = []
    i=0
    while x>0:
        while y[i]<=x:
            lista.append(y[i])
            x-=y[i]
        i=i+1
    return lista
lista1=[500,200,100,50,20,10,5,2,1]
print(funkcja(49,lista1))