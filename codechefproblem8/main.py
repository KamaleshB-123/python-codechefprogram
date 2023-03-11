T = int(input())
for i in range(0, T):
    every_time_complete_levels = 3
    X, Y, Z = input().split(" ")
    a = int(X)/3
    if int(X) % 3 == 0:
      a = a-1

    ans = int(Y) * int(X)
    ex = int(a) * int(Z)
    print(ans + ex)

