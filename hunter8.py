n=int(input())
a=[int(i) for i in input().split()]
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if(a[i]+a[j]==a[k]):
                print(a[i],a[j],a[k])
