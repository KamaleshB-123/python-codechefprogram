
n = int(input())
X = list(map(int, input().split()))
odd_count = 0
even_count = 0
for i in X:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if even_count > odd_count:
    print("READY FOR BATTLE")
else:
    print("NOT READY")

