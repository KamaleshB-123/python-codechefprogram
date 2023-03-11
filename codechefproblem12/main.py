t = int(input())

for i in range(t):
    a, b, c = map(int, input().split(" "))
    lst = [a, b, c]
    lst.remove(max(lst))
    lst.remove(min(lst))
    for j in lst:
        print(j)


