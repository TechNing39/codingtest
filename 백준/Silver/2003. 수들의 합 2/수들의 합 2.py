a,b=map(int,input().split())
arr=list(map(int,input().split()))

left=0
right=0
count=0
sum_num=0

while(True):
    if sum_num<b:
        if right<a:
            sum_num=sum_num+arr[right]
            right+=1
        else:
            break
    elif sum_num>=b:
        sum_num-=arr[left]
        left+=1
    
    if sum_num==b:
        count+=1

    
print(count)
        