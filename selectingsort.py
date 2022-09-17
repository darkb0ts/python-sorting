def select(a):
    if len(a)>1:
        for i in range(0,len(a)):
            min = i
            for j in range(i+1,len(a)):
                if a[min]>a[j]:
                    min = j
            a[min],a[i]=a[i],a[min]
arr = [44, 4, 6, 3, 7, 99, 1, 345, 234, 56, 78, 90,434]
select(arr)
print(arr)
