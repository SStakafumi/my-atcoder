S = str(input())

while True:
    if S[:11] == "dreameraser":
        S = S[11:]
    elif S[:10] == "dreamerase":
        S = S[10:]
    elif S[:7] == "dreamer":
        S = S[7:]
    elif S[:5] == "dream":
        S = S[5:]
    elif S[:6] == "eraser":
        S = S[6:]
    elif S[:5] == "erase":
        S = S[5:]
    elif S == "":
        print("YES")
        break
    else:
        print("NO")
        break

#### 別解 ####
'''
s = input().replace("eraser", "").replace(
    "erase", "").replace("dreamer", "").replace("dream", "")
print("YES" if len(s) == 0 else "NO")
'''
##############