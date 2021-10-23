arr=[3,0,0,2,0,4]
arr=[7,4,0,9]
arr=[8,8,2,4,5,5,1]
n=len(arr)
lx=[]
rx=[]
'''for i in range(n-1):
    lx.append(max(arr[:i+1]))
    rx.append(max(arr[i+1:]))
lx.append(max(arr[ : -1]))
rx.append(arr[n-1])
print(lx,rx)
c=0
for s in range(1,n-1):
    z=(min(lx[s], rx[s]) - arr[s])
    if z>=0:
        c+=z
    print(s,c)
print(c)
'''
c=0
for i in range(1,n-1):
    z=((min ( max(arr[:i+1]), max(arr[i+1:]) )) - arr[i])
    if z>0:
        c+= z
print(c)
