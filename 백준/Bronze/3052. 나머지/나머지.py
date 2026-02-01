array=[]
for _ in range(10):
    num=int(input())
    divided_num=num%42
    array.append(divided_num)
result=list(set(array))
print(len(result))
    