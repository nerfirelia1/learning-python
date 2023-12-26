def insertion(x):
    for i in range(len(x)):
        liczba=x[i]
        while liczba < x[i-1] and i>0:
            x[i-1]=liczba
            i=i-1
    return x
