
T = int(input())

for i in range(0, T):
    X, Y, Z = input().split(" ")
    if int(X) * int(Y) >= int(Z):
        print(int(int(Z)/int(Y)))
    else:
        print(X)

