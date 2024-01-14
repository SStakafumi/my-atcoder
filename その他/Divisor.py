N = int(input())
ans = []


def f(a, b):
    lenA = len(str(a))
    lenB = len(str(b))
    if lenA >= lenB:
        return lenA
    else:
        return lenB


i = 1
while i*i <= N:
    if N % i == 0:
        if i != N // i:
            j = N // i
        else:
            j = i
        ans.append(f(i, j))
    i += 1

print(min(ans))

### nの約数のリストを返す O(√N) ###
'''
def makeDivisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)            
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
'''
