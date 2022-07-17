T=int(input())

for i in range(T):  # 테스트 케이스 번호
    b_lst = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
    k = int(input())  # k층
    n = int(input())  # n호
    for j in range(1, k + 1):  # K층까지 구하겠다 j는 층수
        b_lst.append([])
        for l in range(n):  # n호까지 구하겠다 l+1은 호수
            b_lst[j].append(1)  # 1호는 1밖에 나오지 않으니까 맨 처음에 1을 넣고

            # ----------- 이 반복은 필요 없을 거같은데
            for m in range(1, l + 1):  #
                b_lst[j][m] = b_lst[j][m - 1] + b_lst[j - 1][m]

            # -----------
    print(b_lst[k][n - 1])

