def f(i, r): # 길이 r인 순열을 구하려구요.
    if i==r: # 부분집합 때와 같이, i가 r하고 같아지면(길이 r인 순열을 구하려고 하는 거니까, i는 r만큼 인덱싱해주면서 bit를 변화시킵니다.
        print(bit[:r]) # 프린트를 합니다. 다만 길이 r이므로 [:r]으로 슬라이싱을 해서 프린트해줍니다.
        # all_perm.append(bit[:]) 하면 한번에 모아서 볼 수 있지.
        return # 끝!

    for n in lst: # 순열 안에 들어있는 원소들을 확인한다.
        if n not in bit[0:i]: # i만큼 잘린 bit 안에 원소가 있나요? 헉 없나요?
            bit[i] = n # 그럼 집어넣으세요.
            f(i+1,r) # 그리고 i를 하나 증가시켜 함수 호출.

# N = 4이고 i = 0일 때, n은 0부터 3까지의 원소를 순회하며 for문을 돕니다. 그럼 [0] [1] [2] [3]이 생깁니다.
# 그리고 각각의 [0] [1] [2] [3]은 f(1,r)을 호출합니다. 따라서 방금 전 부분집합에서는 함수를 한 번 만들면 2개씩 아래로 더 생기는 형태였는데,
# 이 경우에는 N개씩 함수가 더 호출됩니다.(재귀)
# 이렇게 호출된 함수가 하나하나 i를 증가시키고, for문을 돌면서 i == r이 되면 print를 합니다.

N = 5 # 순열의 길이
lst = list(range(0, N)) # 순열 안에 들어있는 원소들 리스트로 만들기.
# lst = [3, 4, 5, 8, 9] 뭐 이런 식으로 해서 N = len(lst)로 응용할 수도 있겠지.
bit = [0]*N # 순열의 길이만큼의 bit 리스트를 만든다.
# f(0, N)

for j in range(1, N+1): # 모든 순열을 구하겠어!
    f(0, j) # 여기서 j는 순열의 길이를 의미한다.