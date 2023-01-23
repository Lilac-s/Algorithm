A, B, C = map(int, input().split())
if C <= B:
    print(-1)
else:
    cnt = A // (C-B) + 1
    print(cnt)

    # 3번째 테스트케이스에서 너무 오래 걸림
    '''
    cnt = A // C
    while True:
        cnt += 1
        if A+(B*cnt) < C*cnt:
            break
    print(cnt)
    '''