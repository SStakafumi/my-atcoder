import sys

S = input()
T = input()

for i, s in enumerate(S):
    if T[i] != s:
        print(i+1)
        sys.exit()
print(len(T))