H,M = map(int,input().split())

if M >= 45:
	M -= 45
else: # M이 45분보다 적을 때
	if H == 0:
		H = 23
	else:
		H -= 1
	M = 60 - (45 - M)
print(H,M)