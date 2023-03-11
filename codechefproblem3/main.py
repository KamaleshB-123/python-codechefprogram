
T = input()

for i in range(0, int(T)):
    A, B = input().split(" ")
    C, D = input().split(" ")
    if int(A) < int(C) and int(B) < int(D) or int(A) == int(C) and int(B) == int(D) or int(A) < int(C) and int(B) == int(D) or int(A) == int(C) and int(B) < int(D):
        print("POSSIBLE")
    else:
        print("Impossible")

