def bubble(a):
    if len(a)>1:
        for i in range(0,len(a)):
            for j in range(0,len(a)-1):
                if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]

arr = [44, 4, 6, 3, 7, 99, 1, 345, 234, 56, 78, 90,999]
bubble(arr)
print(arr)
