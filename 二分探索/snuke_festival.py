import bisect

N = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
C = sorted(list(map(int, input().split())))

ans = 0
for mid in B:
    top_num = len(C) - bisect.bisect_right(C, mid)
    bottom_num = bisect.bisect_left(A, mid)
    ans += top_num * bottom_num

print(ans)