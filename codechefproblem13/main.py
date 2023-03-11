t = int(input(" "))

for i in range(t):
    mark_carries = 3
    N, X, Pass_mark = input().split(" ")
    correct_ans_mark = int(X) * mark_carries
    wrong_ans = int(N) - int(X)
    penalty = correct_ans_mark - wrong_ans
    if penalty >= int(Pass_mark):
        print("PASS")
    else:
        print("Fail")
