
T = int(input())

for i in range(0, T):
    A, B, C = input().split(" ")
    if int(A) >= int(B) and int(A) >= int(C):
        print(A)
    elif int(B) >= int(A) and int(B) >= int(C):
        print(B)
    else:
        print(C)
