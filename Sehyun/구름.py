n=int(input('물건의 개수 : '))
d={}

for i in range(n):
    s=input('품명 : ')
    a=int(input('가격 : '))
    b=int(input('개수 : '))
    j=[a,b]
    d[s]=j

for s in d.keys():
    if d[s][1]<3:
        print("3개보다 적습니다.")
    else:
        print('품명:%s,가격:%d,비용:%d'%(s,d[s][0],d[s][0]*d[s][1]))

