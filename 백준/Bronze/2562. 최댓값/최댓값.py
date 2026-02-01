array=[]
for _ in range(9):
    num=int(input())
    array.append(num)

result=max(array)
cnt=0
for i in array:
    if(i==result):
        break
    cnt=cnt+1

print(result)
print(cnt+1)
    