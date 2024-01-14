S = list(input())
T = list(input())

lenS = len(S)
lenT = len(T)
dif = lenT-lenS

if lenS > lenT:
    flag = False

flag = True
cnt = 0

for i, t in enumerate(T):
    if dif - cnt < 0:
        flag = False
        break
    if i <= 1:
        if S[i] != t:
            flag = False
            break
    if i-cnt >= lenS:
        if S[-2] == t and S[-1] == t:
            S.append(t)
        else:
            flag = False
            break
    else:
        if S[i-cnt] != t:
            if S[i-cnt-2] == t and S[i-cnt-1] == t:
                cnt += 1
            else:
                flag = False
                break

if flag:
    print('Yes')
else:
    print('No')
