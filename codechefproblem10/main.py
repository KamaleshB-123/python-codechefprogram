t = int(input())

for i in range(0, t):
    X, Y, D = input().split(" ")
    if (abs(int(X)-int(Y)) <= int(D)):
        print("YES")
    else:
        print("NO")

