import sys


def quick_select(A, k):
    p = A[0]  # 피봇을 리스트의 첫 번째 값으로 설정
    S, M, L = [], [], []  # 피봇보다 작은 값을 저장할 리스트, 피봇과 같은 값을 저장할 리스트, 피봇보다 큰 값을 저장할 리스트
    M.append(p)
    for x in A:  # A의 모든 요소 검사
        if x < p:
            S.append(x)  # 피봇보다 작은 값이면 S에 추가
        elif x > p:
            L.append(x)  # 피봇보다 큰 값이면 L에 추가
        else:
            M.append(x)  # 피봇과 같은 값이면 M에 추가
    if len(S) >= k:
        return quick_select(S, k)
    elif len(S) + len(M) < k:
        return quick_select(L, k - len(S) - len(M))
    else:
        return p


A = list(map(int, sys.stdin.readline().split()))

small = quick_select(A, 1)  # 첫 번째로 작은 값 찾기

if A.index(small) == 0:
    print(0)
else:
    print(len(A) - A.index(small))

'''
비교 횟수 분석

for문에서 리스트 A의 모든 요소를 피봇과 비교해서 값이 큰지, 작은지 검사한다. 이는 리스트의 원소 개수에
비례하므로 C*n만큼 비교하게 된다.(C는 상수) 밑에서 재귀 호출을 하게 되는데 이때 피봇의 값에 따라 수행시간이
달라진다. 좋은 피봇을 골라서 피봇이 중간값이라면 이 경우 비교를 절반만 하게될 수 있으므로
수행시간은 T(n)=T(n/2)+Cn이 된다. 그러나 S 또는 L에 p를 제외한 모든 수가 몰리는 경우에 p를 제외하고 모든 값을
비교해야 하므로 수행시간은 T(n)=T(n-1)+Cn이 된다. 마지막으로 첫 번째로 작은 값의 인덱스를 구한 후,
이 인덱스가 0인지 아닌지 비교하는 연산이 1회 발생한다. 하지만 이는 전체 수행시간에 큰 영향을 미치지 않으므로 무시할 수 있다.
따라서 피봇에 따라 수행시간을 Big-O로 표기하자면 O(n^2)이하 O(n)이상이 된다. 하지만 Quick Select 알고리즘의
평균적인 수행 시간은 O(n)을 보장한다. 따라서 이 알고리즘은 O(n)의 수행시간을 가진다.


'''
