n = int(input())
lst = list()

for _ in range(n):
    a, b = map(int, input().split()) # 왼쪽
    lst.append([a, b])

lst.sort(key=lambda x: x[1])

pos = lst[0][1]
cnt = 1

for i in range(n):
    if lst[i][0] > pos:
        pos = lst[i][1]
        cnt += 1

print(cnt)

'''
알고리즘 및 수행시간 분석

이 프로그램은 강의실 배정 문제와 유사하게 막대의 오른쪽 끝 값을 기준으로 위치를 이동하며 개수를 세면 된다.
오른쪽 끝 값을 기준으로 우선 정렬을 해준다. 이때는 람다를 이용하여 정렬해주었다.(O(logn))
첫 못의 위치는 첫번째 막대가 끝나는 위치로 잡아주고 개수를 하나 세주었다. 이후에는 for문으로 모든 막대를 세보면서
못의 위치보다 왼쪽 끝 값이 오른쪽에 있는 곳으로 위치를 옮겨주고 개수를 하나씩 추가해주었다.

이 코드의 수행시간은 람다를 이용하여 정렬(O(logn))+단일 for문(O(n))이기 때문에 최종 수행시간을 Big-O로 나타내면 O(logn)이 된다.
'''
