T=int(input())

for i in range(1,T+1):
    N,s,e,k=map(int,input().split())

    numbers=list(map(int,input().split()))

    list=numbers[s-1:e]
    list.sort()
    result=list[k-1]

    print(f"#{i} {result}")