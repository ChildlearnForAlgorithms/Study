import sys

sys.setrecursionlimit(100000)

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, k = map(int, sys.stdin.readline().split())
    A = [[0] * M for _ in range(N)]
    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        A[y][x] = 1
    res = k
    for i in range(N):
        for j in range(M):
            if A[i][j] == 1:
                if i == 0:
                    if j != 0 and A[i][j - 1] == 1:
                        res -= 1
                else:
                    if j == 0:
                        if A[i - 1][j] == 1:
                            res -= 1
                    else:
                        if A[i][j - 1] == 1 and A[i - 1][j] == 1 and A[i - 1][j - 1] == 0:
                            res -= 2
                        elif A[i][j - 1] == 1 or A[i - 1][j] == 1:
                            res -= 1
    for i in range(N):
        print(A[i])
    print(res)
'''
1
5 5 7
3 0
3 1
3 2
2 2
1 2
0 2
1 1

1
6 6 10
0 2
1 0
1 1
1 2
2 1
3 4
4 4
4 3
4 5
5 4

1
1 3 2
0 0
0 2

1
10 8 18
0 0
1 0
1 1
2 0
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6

2
10 5 4
0 0
0 1
9 0
9 1
5 10 4
0 0
1 0
0 9
1 9

2
15 15 21
0 3
0 12
1 12
1 14
2 1
2 10
2 11
3 6
4 1
5 4
6 10
6 13
7 7
9 3
9 4
10 3
10 10
10 11
12 1
12 9
14 14
15 15 80
0 0
0 1
0 4
0 10
1 2
1 7
1 10
1 12
1 13
2 2
2 3
2 7
3 2
3 4
3 6
3 8
3 11
3 14
4 0
4 1
4 2
4 5
4 6
4 7
4 8
4 11
4 12
4 14
5 0
5 2
5 4
5 7
5 8
5 10
5 11
5 13
5 14
6 5
6 10
6 12
6 13
6 14
7 1
7 9
7 12
7 13
8 2
8 4
8 8
8 9
8 12
8 13
9 0
9 3
9 5
9 11
10 2
10 3
10 5
10 9
10 10
11 8
11 9
11 11
11 12
11 13
12 3
12 13
12 14
13 1
13 4
13 7
13 9
13 10
13 13
14 0
14 5
14 7
14 8
14 13

1
2 2 3
0 0
1 1
0 1
'''
