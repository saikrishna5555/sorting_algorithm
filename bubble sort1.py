a=[1,2,8,4,9,90]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]

print(a)
#time complexity o(n2)
#space o(1)
