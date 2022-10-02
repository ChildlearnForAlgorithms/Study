import heapq  # heapq 모듈을 불러옴.
from sys import stdin  # 실행 속도를 빠르게 하기 위해 sys 모듈의 stdin을 불러옴.

A = list(map(int, stdin.readline().split()))  # 리스트 생성.

ans = 0  # m[i]의 값을 담을 변수를 초기화해줌.
max_heap = []  # max-heap을 생성해줌.
min_heap = []  # min-heap을 생성해줌.

for idx, val in enumerate(A,start=1):  # 파이썬의 enumerate() 함수를 이용해 인덱스와 원소를 동시에 접근하면서 루프를 돌림. 이때 가장 작은 원소를 1번째로 작다고 정의하기로 했으니까 시작 인덱스를 1로 변경.
    if min_heap and (idx != 1 and idx % 3 == 1):  # min-heap이 비어있지 않고 인덱스가 1이 아니고(시작 원소니까) 3으로 나눈 나머지가 1일 때
        val2 = heapq.heappop(min_heap)  # heapq.heappush(max_heap,(-heapq.heappop(min_heap),heapq.heappop(min_heap))으로 해주면 최대 힙에 push 할 때 우선 순위에 따라 순서가 바뀌므로 먼저 따로 변수를 생성하여 최소 힙의 원소를 pop 해줌.
        heapq.heappush(max_heap, (-val2, val2))

    heapq.heappush(max_heap, (-val,val))  # heapq 모듈은 최소 힙을 기능만으로 동작하기 때문에 최대 힙으로 활용하려면 힙에 튜플을 원소로 추가하거나 삭제하면, 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리를 이용함. 따라서, 최대 힙을 만들려면 각 값에 대한 우선 순위를 구한 후, (우선 순위, 값) 구조의 튜플을 힙에 추가해줌.
    val3=heapq.heappop(max_heap)[1] # 힙에서 값을 읽어올 때는 우선 순위에는 관심이 없으므로 각 튜플에서 인덱스 1에 있는 값을 취함.
    heapq.heappush(min_heap, val3)  # 최대 힙에서 pop 했던 값을 최소 힙에 넣어줌.
    ans += min_heap[0]  # min-heap의 첫 번째 원소를 ans 변수에 저장해줌.

print(ans)  # 답을 출력.

'''
사용한 자료구조 및 알고리즘 분석

max-heap과 min-heap 총 2개의 힙을 이용해 i//3+1번째 작은 수를 찾도록 하였다. heap은 우선순위 큐이므로 pop을 하면 0번째 원소가 삭제되면서 반환되는 성질을 이용하였다.
idx != 1 and idx % 3 == 1 이 아닐 때는 최대 힙에 넣고, 그 다음 최대 힙의 원소를 pop 하여 최소 힙에 넣는다. 이를 idx != 1 and idx % 3 == 1을 만족할 때까지 반복한다. 
반복하면서 최소 힙에는 원소가 계속 저장된다. idx != 1 and idx % 3 == 1을 만족하는 인덱스 값을 만나면 최소 힙의 원소를 pop하여 최대 힙에 넣고, idx != 1 and idx % 3 == 1을 만족하는 인덱스의 val 값을
최소 힙에 넣어서 i//3+1번째로 작은 수를 찾을 수 있도록 하였다. for문이 돌아갈 때마다 최소 힙의 첫 번째 원소를 변수에 저장 후, 최종적으로 그 변수의 값을 출력해 준다.

수행시간 분석

for문 내부의 heappop()과 heappush()는 O(log(n))의 시간 복잡도를 가진다.
이는 힙의 높이(h)가 리스트 원소의 개수가 n개일 때, 2^0+2^1+.......+2^(h-1)+2^(h-2)=2^h-1=n이기 때문에 양변에 로그를 취하여 시간 복잡도를 구해보면 O(log(n))이기 때문이다.
for문은 리스트의 길이만큼 돌아가므로 수행시간은 리스트 원소의 개수에 비례하기 때문에 O(n)의 시간 복잡도를 가진다.
for문은 내부의 heappop() 및 heappush() 및 여러 연산을 감싸고 있기 때문에 이 코드의 수행시간을 표현해보면 T(n)=n*logn+C(C는 상수)이다.
따라서 이 코드의 수행시간을 Big-O로 표기하면 O(nlog(n))이 된다.

'''
