N = int(input())
A = list(map(int, input().split()))

A.reverse()
lenA = int(len(A))
lefta = 0
sum = 0

for a in A:
    sum += a
    if sum <= 3:
        lefta += 1
    else:
        break

print(lenA-lefta)
