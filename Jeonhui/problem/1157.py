s=input().strip()
s_upper=s.upper()
import collections
s_list=collections.Counter(s_upper)
values=[i for i in s_list.values()]
values.sort(reverse=True)
big=values[0]
result=[i for i,k in s_list.items() if big==k]
if len(result)!=1:
    print('?')
else:
    print(result[0])