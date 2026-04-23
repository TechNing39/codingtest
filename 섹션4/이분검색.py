# 기존 풀이 - 선형 탐색 O(n)
n,m=map(int,input().split())
arr=list(map(int,input().split()))
sorted_arr=sorted(arr)

for idx,i in enumerate(sorted_arr):
   if i==m:
       print(idx+1)


# 개선 풀이 - 이진 탐색 O(log n)
n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()

l=0
r=n-1
mid=n//2

while l<=r:
    mid=(l+r)//2
    if arr[mid]==m:
        print(mid+1)
        break
    elif arr[mid]<m:
        l=mid+1
    else:
        r=mid-1
