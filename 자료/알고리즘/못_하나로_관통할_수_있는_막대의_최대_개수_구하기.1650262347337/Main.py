import sys

n = int(sys.stdin.readline())
d = {}

for i in range(n):
	s, e = map(int, sys.stdin.readline().split())
	if s not in d:
		d[s] = "["
	else:
		d[s] = "[" + d[s]
	if e not in d:
		d[e] = "]"
	else:
		d[e] = d[e] + "]"
		
all_pos = sorted(d.keys())
all_stick = ""

for pos in all_pos:
	all_stick += d[pos]
	
max_cnt, cnt = 0, 0

for i in all_stick:
	if i == "[":
		cnt += 1
	elif i == "]":
		cnt -= 1
	if cnt > max_cnt:
		max_cnt = cnt
	
print(max_cnt)
'''
시작값을 '[', 끝 값을 ']'으로 생각하고
가장 많은 괄호 안에 있는 값이 가장 많은 막대가 겹치는 부분이다.
탐색이 빠른 자료구조인 딕셔너리를 이용하여 작성하였다.
같은 위치에 시작값이나 끝값을 가지는 선분은 그 시작값과 끝값을 포함하기 때문에
[를 저장할 때는 기존의 값의 앞에 저장을 하고, ]를 저장할 때는 기존의 값의 뒤에 저장을 한다.
이 딕셔너리의 키값들을 정렬하고, 정렬한 순서대로 그 값들을 가져오면
막대들이 포함하는 분들을 알 수 있다.
막대들이 가장 많은 점의 막대들의 개수를 찾는 것이므로 [일 때는 cnt를 1 증가 시키고,
]일 때는 1을 감소 시키는 방식으로 겹치는 부분의 막대의 개수를 찾을 수 있다.
그 중 가장 큰 값이 정답이다.

수행시간은 
값을 입력받기 위해 Cn의 시간이 걸리고,
딕셔너리에 저장한 키값들을 정렬하기 위해
위치의 개수는 최대 2n개이므로 최대 (2Cn)log(2Cn)의 시간이 걸린다.
그리고 딕셔너리의 값을 합치는 것과 최대값을 계산하는 것에 각각 2Cn의 시간이 걸린다.
T(n) = Cn + (2Cn)log(2Cn) + 2Cn + 2Cn +C 이므로
O(n)이다.

'''