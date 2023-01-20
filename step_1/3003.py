b_chess_list = [1, 1, 2, 2, 2, 8]
w_chess_list = map(int, input().split())

lst = [b - w for b, w in zip(b_chess_list, w_chess_list)]
result = " ".join(map(str, lst))

print(result)