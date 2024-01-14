N = int(input())
# 一旦setにしたあとにlistに戻すと重複したやつを取り除くことができる
print(len(list(set([int(input()) for _ in range(N)]))))
