import sys

n = int(sys.stdin.readline())
lst = list()  # 리스트 생성

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lst.append([a, "f"])  # 리스트에 시작점과 first를 나타낼 'f'를 묶어 삽입
    lst.append([b, "l"])  # 리스트에 끝점과 last를 나타낼 'l'를 묶어 삽입

lst.sort(key=lambda x: (x[0], x[1]))  # 리스트를 시작점과 끝점을 모두 모아 오름차순으로 정렬한 뒤, 같은 값끼리는 'f'가 앞에 오도록 정렬

cnt, max_cnt = 0, 0

for i in range(2 * n):
    if lst[i][1] == "f":  # 왼쪽 끝 점이면 수직선이 통과하는 막대 개수 1 증가
        cnt += 1
    if lst[i][1] == "l":  # 오른쪽 끝 점이면 수직선이 통과하는 막대 개수 1 감소
        cnt -= 1
    max_cnt = max(cnt, max_cnt)  # 계속해서 max_cnt값을 가장 큰 cnt 값으로 초기화 시켜줌

print(max_cnt)

'''
알고리즘 및 수행시간 분석

막대기들을 수직선상에 있다고 생각한 뒤 못을 계속해서 오른쪽으로 옮겨주며 최대 막대 수를 계산할 수 있다. 
왼쪽 끝 점을 만나면 개수가 하나 늘고, 오른쪽 끝 점을 지나면 통과하는 막대기의 개수가 줄어든다.
리스트에 왼쪽 끝 점과 오른쪽 끝 점을 넣어줄 때 시작점인지 끝점인지 구분할 수 있도록 각각 'f'와 'ㅣ'을 함께 넣어주었다.
그리고 람다를 이용하여 정렬해준 후, 왼쪽 끝 점이면 수직선이 통과하는 막대 개수를 증가시켜주었고, 오른쪽 끝 점이면
수직선이 통과하는 막대 개수를 감소시켜 주었다. 

이 코드의 수행시간은 람다를 이용하여 정렬(O(nlogn))+ 정렬 순서대로 한 번씩 고려하는 선행 스캔(O(n))이면 되기 때문에
최종 수행시간을 Big-O로 나타내면 O(nlogn)이 된다.

'''
