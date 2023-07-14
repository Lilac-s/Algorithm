# 트리 노드 클래스 정의
class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

# 전위 순회 함수


def preorder(node):
    if node:
        print(node.item, end='')
        preorder(node.left)
        preorder(node.right)

# 중위 순회 함수


def inorder(node):
    if node:
        inorder(node.left)
        print(node.item, end='')
        inorder(node.right)

# 후위 순회 함수


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.item, end='')


# 트리 생성
n = int(input("노드 개수 입력: "))
inputs = []
for _ in range(n):
    node_input = input("노드 정보 입력 (아이템 왼쪽자식 오른쪽자식): ").split()
    inputs.append(node_input)

tree = {}
for item, left, right in inputs:
    tree[item] = Node(item, left, right)

# 전위 순회 출력
print("전위 순회:", end=' ')
preorder(tree['A'])
print()

# 중위 순회 출력
print("중위 순회:", end=' ')
inorder(tree['A'])
print()

# 후위 순회 출력
print("후위 순회:", end=' ')
postorder(tree['A'])
print()
