t = int(input())

for i in range(0, t):
    x1, y1, x2, y2 = input().split(" ")
    X = int(x1) - int(x2)
    Y = int(y1) - int(y2)
    if "-" in str(X) or str(Y):
        X = str(X).replace("-", "")
        Y = str(Y).replace("-", "")

    maximum_value = max(int(X), int(Y))
    print(maximum_value)
