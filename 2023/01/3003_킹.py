king, queen, rook, bishop, knight, pawn = map(int, input().split())
res = [1-king, 1-queen, 2-rook, 2-bishop, 2-knight, 8-pawn]
res_to_str = list(map(str, res))
print(" ".join(res_to_str))