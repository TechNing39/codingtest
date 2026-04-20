N=int(input())
K=int(input())

index=1
count=0
array=[]

while index<=N:
    if N%index==0:
        count+=1
        array.append(index)
    index+=1

try:
    result=array[K-1]
    print(result);
except Exception as e:
    print(-1)
