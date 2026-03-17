N=int(input())
num=list(map(int,input().split()))
B,C=map(int,input().split())
count=0
for i in num:
    i=i-B
    if i>0 and i<C:
        count+=1
    elif i>0 and i>=C:
        count+=i // C
        if i % C != 0:
            count += 1
print(count+N)

