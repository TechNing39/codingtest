N=int(input())
s,m,l,xl,xxl,xxxl=map(int,input().split())
size_list=[s,m,l,xl,xxl,xxxl]
t,p=map(int,input().split())
bundle=0
for count in size_list:
    if(count==0):
        continue

    if count%t==0:
        bundle+=(count//t)
    else:
        bundle+=(count//t)+1
        
        
print(bundle)
print(N//p,N%p)