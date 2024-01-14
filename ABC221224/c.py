S = input()

cnt = 0
i = 0

while i < len(S):
    if int(S[i]) != 0:
        cnt += 1
        i += 1
    elif int(S[i]) == 0:
        if i == len(S)-1:
            cnt += 1
            i += 1
        else:
            if int(S[i+1]) != 0:
                cnt += 1
                i += 1
            else:
                cnt += 1
                i += 2


print(cnt)              