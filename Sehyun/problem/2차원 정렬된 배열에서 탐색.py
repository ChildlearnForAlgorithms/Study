import sys

n, k = map(int, sys.stdin.readline().split())

lst = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

bool = False  # 이진탐색을 통해 값을 발견했는 지 확인하기 위한 변수


def binary_search(A, k):  # 리스트 A에서 값 k 찾기
    global bool  # global을 이용해 전역 변수로 사용
    l, r = 0, n - 1  # 왼쪽 인덱스와 오른쪽 인덱스
    while r - l >= 0:  # 오른쪽 인덱스가 왼쪽 인덱스보다 크거나 같을 때까지 검사
        m = (l + r) // 2  # 가운데 값
        if A[m] > k:  # 찾으려는 값보다 리스트의 중앙값이 클 경우
            r = m - 1  # 리스트의 왼쪽에서 탐색
        elif A[m] < k:  # 찾으려는 값이 리스트의 중앙값보다 클 경우
            l = m + 1  # 리스트의 오른쪽에서 탐색
        elif A[m] == k:  # 찾으려는 값이랑 리스트의 중앙값이 같을 경우
            bool = True  # 값을 발견했으므로 bool 값을 True로 변경
            return m  # 값의 인덱스 반환


m = 0

for i in range(n):
    A = lst[i]  # 리스트 A의 i번째 줄을 탐색
    for j in range(n):
        m = binary_search(A, k)
    if bool == False:
        continue
    elif bool == True:  # k 값이 (i,j)에 있다면 출력
        print((i, m))
        break

if bool == False:  # k 값이 (i,j)에 없다면
    print((-1, -1))

'''
알고리즘 설명 : 
이차원 nxn 리스트를 각 줄마다 binary_search 함수를 이용하여 값이 있는지 찾았다. 값을 찾았는지 확인하기 위해
bool이라는 변수를 False 값으로 우선 초기화 해주었다. for문을 이용해 각 줄마다 검사하였을 때 값을 찾은 경우에는
bool 값을 True로 바꿔주었고, 값의 인덱스를 출력하도록 하였다. 각 줄에서 값을 찾지 못한 경우에는 다음 줄로 넘어가서
다시 이진 탐색을 통해 값을 검사하였다. 만약 모든 for문을 다 돌았을 경우에도 값을 찾지 못한 경우에는 (-1, -1)을 출력해줬다.

수행시간 분석 : 
binary_search 함수의 시간 복잡도부터 구해본다면 최악의 경우는 남은 데이터가 하나가 될 때까지 탐색을 반복하는 것이다.
전체 데이터 수를 N이라고 한다면 첫 번째 탐색 후 절반만 남아 남은 수가 N/2개, 두 번째 탐색에서 다시 절반만 남아 남은 수가 
N/2*1/2개. 세 번째 탐색에서 다시 절반이 남아 남은수가 N/2*1/2*1/2개. 규칙을 찾으면 k번째 탐색에서 남은 데이터 수는
(1/2)**k*N이 된다. 최악의 경우에선 (1/2)**k*N=1이 된다. 위 식의 양 변에 2**k를 곱하면 2**k=N이 되고 양 변에 log를
취하면 최종 식은 k=logN이 된다. 따라서 이진 탐색의 시간 복잡도는 O(logn)이 된다. binary_search 함수를 이중 for문이
감싸고 있으므로 최종 시간 복잡도는 O(n*2logn)이 된다. 중간 과정의 시간 복잡도에 영향을 미치지 않는 연산들은 모두 상수 취급하였다.

'''
