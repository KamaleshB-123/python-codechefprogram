t = int(input(""))
for i in range(t):
    count = 0
    n = int(input(""))
    a = list(map(int, input().split(maxsplit=int(n)-1)))
    for j in a:
        if 10 <= j <= 60:
            count += 1
    print(count)
