import sys
n=int(sys.stdin.readline())
S=sorted(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
card=list(map(int,sys.stdin.readline().split()))
index,m_dic=0,{}
for m in sorted(card):
    cnt=0
    if m not in m_dic:
        while index<len(S):
            if m==S[index]:
                cnt+=1
                index+=1
            elif m>S[index]:
                index+=1
            else:
                break
        m_dic[m]=cnt
print(' '.join(str(m_dic[m]) for m in card))



