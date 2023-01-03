import sys
sys.stdin= open('input.txt')

# 노드 번호가 i인 노드의 부모 노드 번호 i/2
def inorder(T):
    if T > N:
        return
    if (T*2) <= N: # 노드 번호가 i인 노드의 왼쪽 자식 노드 번호 2*i
        inorder(T*2)
    res.append(node[T])
    if (T*2+1) <= N: # 노드 번호가 i인 노드의 오른쪽 자식 노드 번호 2*i+1
        inorder(T*2+1)

for tc in range(1, 11):
    N = int(input())
    node = [0]*(N+1)
    for _ in range(N):
        lst = input().split()
        node[int(lst[0])] = lst[1]
    print(node)
    res = []
    inorder(1)
    print(f'#{tc} {"".join(res)}')
