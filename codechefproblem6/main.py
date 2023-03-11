t=int(input())
for i in range(t):
    a,b=list(map(int,input().split()))
    if(a<=b):
        print(a)
    else:
        print(a+(a-b))
