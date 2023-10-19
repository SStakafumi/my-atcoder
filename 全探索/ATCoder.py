S = input()

ans = 0
tmp = 0
for s in S:
    if s in ['A', 'C', 'G', 'T']:
        tmp += 1
    else:
        tmp = 0
    ans = max(ans, tmp)
        
print(ans)


