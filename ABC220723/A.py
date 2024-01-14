l1, r1, l2, r2 = map(int,input().split())

l = [0]*101

for i in range(l1, r1):
    l[i] += 1

for j in range(l2, r2):
    l[j] += 1
    
print(l.count(2))