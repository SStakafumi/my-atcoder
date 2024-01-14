### TLE回答 ###
'''
N = int(input())
S = str(input())
ans = 0

for i in range(10):
    for j in range(10):
        for k in range(10):
            key = str(i) + str(j) + str(k)
            for s in S:
                if s == key[0]:
                    key = key[1:]
                    if key == "":
                        ans += 1
                        break

print(ans)
'''

### 解法1 単純に部分数列を求める###
'''
n = int(input())
s = input()
d1 = set()
d2 = set()
d3 = set()
for c in s:
    for t in d2:
        d3.add(t + c)
    for t in d1:
        d2.add(t + c)
    d1.add(c)
    # print(d1, d2, d3)
print(len(d3))
'''

### 解法2 ###


from bisect import bisect
n = int(input())
s = input()

location = [[] for _ in range(10)]
# enumrate() : イテラブルオブジェクトを引数に指定しインデックス番号、要素の順に取得できる

for i, c in enumerate(map(int, s)):
    location[c].append(i)

maxLocation = [loc[-1] if loc else -1 for loc in location]
ans = 0

for loc_x in location:
    if not loc_x:
        continue  # 要素がなければforに戻る すなわちこの数字(index)は文字列sに存在せず10*10*10で調べるまでもない
    i = loc_x[0]
    for loc_y in location:
        ji = bisect(loc_y, i)  # リストloc_yに対し引数iよりも大きい値の中で最小の値のインデックスをjiに格納
        if ji == len(loc_y):  # 要素がなければ([]の状態)forに戻る すなわちこの数字(index)は文字列sに存在せず10*10*10で調べるまでもない
            continue
        j = loc_y[ji]  # より大きい値の中で最小の値をjに格納
        ans += sum(j < li for li in maxLocation)

print(ans)
