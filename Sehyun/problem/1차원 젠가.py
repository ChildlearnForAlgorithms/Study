n=int(input())
lst=[]
for _ in range(n):
    num=int(input())
    lst.append(num)


end_of_array=n
def block(a,b):
    global end_of_array
    index_lst=[]
    temp=[]

    for i in range(a-1,b):
        index_lst.append(i)

    for i in range(end_of_array):
        if i not in index_lst :
            temp.append(lst[i])

    for i in range(len(temp)):
        lst[i]=temp[i]
    end_of_array=len(temp)

for _ in range(2):
    a,b=map(int,input().split())
    block(a,b)

print(end_of_array)
for i in range(end_of_array):
    print(lst[i])

