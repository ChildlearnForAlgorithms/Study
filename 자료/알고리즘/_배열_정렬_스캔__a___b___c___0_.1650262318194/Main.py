import time

#O(n)과 O(nlogn)의 시간 복잡도를 가지는 two_sum함수
def two_sumNlogN(X, Y, t):
    # x+y=t을 찾기
    for y in Y:
        A = X  # A에 X배열을 저장
        while len(A) != 0:  # logn번
            i = len(A) // 2  # i를 A의 배열의 인자 개수의 절반으로 설정
            if A[i] > (t - y):
                A = A[:i]
                # A[i]가 (t-y)보다 크면 A의 범위를 0부터 i까지 설정
            elif A[i] == (t - y):
                return True
            # A[i]와 t-y의 값이 같으면 True 반환
            else:
                A = A[i + 1:]
            # A[i]가 (t-y)보다 작으면 A의 범위를 i+1부터 마지막으로 설정
    return False
# 수행시간 분석 및 Big-O 표기
# median of medians를 활용하여 만든
# O(nlogn)의 two_sum 알고리즘이다.
# A만 정렬되어있어도 이용가능 하다.
# Worst Case는 조건에 맞는 값이 없고 if문만 계속 실행되는 경우이다.
# 이 경우의 T(n)=n+n*5*logn이다.
# 시간복잡도는 O(n)이다.


def two_sum(X, Y, t):
    # x+y=t을 찾기
    i, j = 0, len(Y) - 1  # =연산과 -연산 3회

    # len(X)와 len(Y)의 합만큼 반복 즉, 2n번 반복
    for _ in range(len(X) + len(Y)):
        if X[i] > t - Y[j]:
            j -= 1
        # X[i]가 t-Y[j]보다 크면 j를 1 감소하여 t-T[j] 더 큰 수를 가리킨다.
        elif X[i] < t - Y[j]:
            i += 1
        # X[i]가 t-Y[j]보다 크면 i를 1 증가하여 X[i]가 더 큰 수를 가리킨다.
        else:
            return True
        # X[i]가 t-Y[j]와 같으면 True를 반환한다.
        if i >= len(X) or j < 0:
            break
        # X또는 Y배열의 인자들을 모두 확인하면 반복문을 탈출한다.
    return False
    # 반복문을 나왔을 경우 조건에 맞는 값이 없으므로 False 반환


# 수행시간 분석 및 Big-O 표기
# worst case는 모든 반복이 실행 되었을 때 즉, i=len(X)-1이고 j=0이 될 때이다.
# 이 경우 if문이 >,-,=연산으로 4번 연산하고
# elif문이 if문에서 >,-연산을 하고 지나와서 <,-,+,= 연산을 4번하여 총 6번 연산한다.
# 마지막 if문은 >=,or,<까지 4번 연산을 한다.
# X와 Y의 길이가 각각 n이라 했을 때
# T(n)=4n+6n+3n=13n
# 시간복잡도는 O(n)이다.

# 시간을 비교하는 함수
def timeCheck(A, B, C):
    A.sort()

    s1 = time.perf_counter()
    for t in C:
        if two_sum(A, B, t * -1):
            break
    e1 = time.perf_counter()
    print("O(nlogn) : " + s1 + " " + e1)

    B.sort()

    s2 = time.perf_counter()
    for t in C:
        if two_sum(A, B, t * -1):
            break
    e2 = time.perf_counter()
    print("O(n) : " + s2 + " " + e2)


if __name__ == '__main__':
    A = list(map(int, input().split()))  # A 입력
    B = list(map(int, input().split()))  # B 입력
    C = list(map(int, input().split()))  # C 입력

    # timeCheck(A,B,C)

    A.sort()  # A 정렬
    B.sort()  # B 정렬
    # 파이썬의 sort함수는 O(nlogn)

    result = False  # 결과를 저장할 배열

    for t in C:  # n번
        if two_sum(A, B, t * -1):
            result = True
            break
    # a+b+c=0에 만족하는 수가 있으면 True를 출력하고 반복문을 탈출
    print(result)  # 결과를 출력