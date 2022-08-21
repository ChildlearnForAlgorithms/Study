n = int(input())  # 반복 횟수
for _ in range(n):
    c, a = map(int, input().split())  # 개수, 몇 번째로 인쇄 궁금한 문서 위치
    q = list(map(int, input().split()))
    cnt = 0
    while len(q) != 0:
        if q[0] < max(q):
            q.append(q.pop(0))
            a = (a - 1 if a > 0 else len(q) - 1)
        else:
            q.pop(0)
            cnt += 1
            if a == 0:
                break
            a = (a - 1 if a > 0 else len(q) - 1)
    print(cnt)
