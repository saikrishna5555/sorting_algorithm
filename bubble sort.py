a=list(map(int,input().split()))
for i in range(len(a)):
    flag=True
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            flag=False
    if flag:
        break
print(a)



# time complexcity o(n^2) in worst case
#  o(1)