rule = 107/100
n = int(input())
for i in range(0, n):
    X, Y = input().split(" ")  # single line of input, two space separated integers X and Y
    X = int(X) * rule
    if X > int(Y) or X == int(Y):
        print("YES")
    else:
        print("NO")
