<<<<<<< HEAD
import sys
a= sys.stdin.readline().split()
print(a[0][::-1] if int(a[0][::-1]) > int(a[1][::-1]) else a[1][::-1])
=======
a,b=input().split()
a_list=list(a)
b_list=list(b)
a_list.reverse()
b_list.reverse()
a2=''.join(a_list)
b2=''.join(b_list)
print(max(a2,b2))
#커밋
>>>>>>> cec8d9b82b4579bbbcd8ccb3f32835ec58b6b308
