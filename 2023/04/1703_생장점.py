while 1:
    leafs = list(map(int, input().split())) 
    leaf = 1
    if leafs[0] == 0:
        break
    for i in range(1, len(leafs), 2):
        leaf = leaf * leafs[i] - leafs[i+1]
    print(leaf)