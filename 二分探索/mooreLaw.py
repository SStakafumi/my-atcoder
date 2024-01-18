import math

P = float(input())

def is_ok(arg):
    return 1-(2/3)*P*math.log(2)*2**(-2*arg/3) <= 0

def meguru_bisect(ng, ok):
    while abs(ok-ng) >= 1e-8:
        mid = (ok+ng)/2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

startTime = meguru_bisect(0, 1e+18+1)
print(startTime+P*2**(-2*startTime/3))