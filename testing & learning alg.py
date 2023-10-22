n=[2,5,23,2,1,0]
def bubble_sort(n:list)-> list:
    for i in range(len(n)-1):
        for j in range(len(n)-i-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    return n
print(bubble_sort(n))