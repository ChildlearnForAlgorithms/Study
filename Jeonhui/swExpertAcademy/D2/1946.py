T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    strRes = ""
    for i in range(n):
        ch,cnt = input().split()
        strRes += ch*int(cnt)
    prev = 0
    for i in range(10,len(strRes)+10,10):
        print(strRes[prev:i])
        prev = i
        print(i)