T = int(input())
d = {}
for i in range(26):
    d[chr(65 + i)] = i
for i in range(26):
    d[chr(97 + i)] = d['Z'] + i + 1
for i in range(10):
    d[str(i)] = d['z'] + i + 1
d['+'], d['/'] = d['9'] + 1, d['9'] + 2
for test_case in range(1, T + 1):
    inStr = input()
    outStr = ''
    decode = 0b0
    for i in range(len(inStr)):
        decode <<= 6
        decode |= (d[inStr[i]] & 0x3F)
        if i % 4 == 3:
            outStr += chr((decode >> 16) & 0xFF) + chr((decode >> 8) & 0xFF) + chr(decode & 0xFF)
            decode = 0b0
    print(f"#{test_case} {outStr}")
