def comb(arr, n): # 조합 구현
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            # arr[i+1:]은, i로 결정된 앞쪽을 제외한 나머지 부분을 뜻한다.
            # i로 조합의 한 부분이 결정되었으니,
            # comb의 인자 n은 하나 줄어들어서 n-1이 된다.
            for j in comb(arr[i + 1:], n - 1):
                # print(f'{i}번째, {arr}와{n}, {j}에서 돌고 있어')
                # result.append로 넘어가기 전에 j를 정하기 위해 재귀함수가 돌겠구나.
                # 재귀함수를 타고 들어가서 마지막 재귀함수에서 n == 1이 되면,
                # for 문 전에 if n == 1:에서 걸려서 result.append가 될 거고,
                # 그렇게 첫 result가 return되면 그때부터 j가 결정되어서
                # 위에 있는 재귀함수들이 마무리되기 시작하겠네.
                result.append([arr[i]] + j)
    # 마지막 result가 return되면 함수가 끝난다.
    return result

def perm(arr, n): # 순열 구현
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in perm(ans, n-1):
                result.append(arr[i]+p)

arr = [1, 2, 3, 4, 5]
print(comb(arr, 1))
print(comb(arr, 3))
print(comb(arr, 3))
print(perm(arr, 3))