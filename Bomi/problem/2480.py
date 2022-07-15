one, two, three = map(int, input().split())
winning_price = 0

if one == two == three: # 세 주사위의 눈이 같은 경우
	winning_price = 10000 + 1000 * one

# 두 주사위의 눈이 같은 경우
elif (one == two) and (one != three): # one 과 two 의 눈이 같음
	winning_price = 1000 + 100 * one
elif (two == three) and (two != one): # two 와 three 의 눈이 같음
	winning_price = 1000 + 100 * two
elif (one == three) and (one != two): # one 과 three 의 눈이 같음
	winning_price = 1000 + 100 * one

# 어떤 주사위도 눈이 같지 않음
elif (one != two) and (two != three):
	winning_price = 100 * max(one, two, three)

print(winning_price)