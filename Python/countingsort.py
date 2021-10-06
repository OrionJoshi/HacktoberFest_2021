#  both were stable... not sure!~

def ctsrt(li):
    d={}
    li2=[]
    for i in li:
        if i not in d:d[i] = 0
        d[i]+=1
    k=0
    m=0
    for i in d.keys():
        if m == 0:
            k=d[i]
            m=1
            continue
        d[i]+=k
        k=d[i]
    li2=li[:]
    for i in reversed(li):
        li2[d[i]-1]=i
        d[i]-=1
    print(li2)

ctsrt([1,2,3,5,3,2,1,5,7,3,5,6])
