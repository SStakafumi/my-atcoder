N, M = map(int, input().split())

A = list(map(int, input().split()))
all_cards_sum = sum(A)
circular_m = list(map(lambda x: (x % M, x//M), A))
circular_m.sort()

# print(circular_m)

prev_m_mod, prev_m_div = circular_m[0]
# 最小の数
tmp_dispose = prev_m_mod + prev_m_div*M
max_dispose = tmp_dispose

first_flag = True
first_dispose = 0
# zero start
for m_mod, m_div in circular_m[1:]:
    if not (0 <= m_mod-prev_m_mod <= 1):
        if first_flag:
            first_dispose = tmp_dispose
            first_flag = False

        if tmp_dispose > max_dispose:
            # print("Updated", tmp_dispose)
            max_dispose = tmp_dispose
        tmp_dispose = 0

    tmp_dispose += m_div*M + m_mod
    prev_m_mod = m_mod
    prev_m_div = m_div

# print("Updated", tmp_dispose)
max_dispose = max(max_dispose, tmp_dispose)

# 循環 start
first_m_mod, first_m_div = circular_m[0]
last_m_mod, last_m_div = circular_m[-1]

if first_m_mod == 0 and last_m_mod == (M-1):
    tmp_dispose += first_dispose
max_dispose = max(max_dispose, tmp_dispose)

# print(all_cards_sum)
# print(max_dispose)
print(all_cards_sum - max_dispose)
