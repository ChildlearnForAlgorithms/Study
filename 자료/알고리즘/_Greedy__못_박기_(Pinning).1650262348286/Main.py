import sys

n = int(sys.stdin.readline())
stick = []
for i in range(n):
	stick.append(list(map(int, sys.stdin.readline().split())))
stick.sort(key=lambda x: x[1])
pin = 1
pin_pos = stick[0][1]
for i in range(1, n):
	if stick[i][0] > pin_pos:
		pin_pos = stick[i][1]
		pin += 1
print(pin)

'''
stick을 끝 점에 대해 오름차순을 정렬을 한 뒤
가장 작은 끝 점에서 pin을 사용해야하기 때문에
pin의 초기값은 1을 주고 pin_pos는 가장 작은 끝 점을 준다.
가장 작은 끝 점이기 때문에 다른 stick의 시작점이 pin_pos보다 작을 경우
현재의 pin_pos지점에 pin이 꼽힌다. 이후 시작점이 pin_pos보다 클 경우
앞선 stick의 값들은 이미 사라져있고, 기존의 pin_pos로 stick을 없앨 수 없으므로
pin을 하나 증가시킨뒤 pin_pos의 위치를 이 stick의 끝값으로 바꿔준다.
수행시간은 내림차순으로 정렬을 하기위해 nlogn의 수행시간을 가지고,
pin의 개수를 찾기 위해 n번의 반복을 수행한다 이를 식으로 나타내면
T(n) = O(nlogn) + Cn + C 이다.
결론적으로 수행시간은 O(nlogn)이다.
'''