arr=[]
new_arr=[]
second_new_arr=[]
result_arr=[]
reversed_arr=[]
count=0
for _ in range(7):
    arr.append(list(map(int,input().split())))

for i in range(7):
    new_arr.append(arr[i])
p=0
for i in range(7):
    for j in range(7):
        second_new_arr.append(arr[j][i])
    for m in range(3):
        result_arr=second_new_arr[m:m+5]
        reversed_arr=result_arr[::-1]
        if result_arr==reversed_arr:
            count=count+1
    second_new_arr=[]

result_arr=[]

for j in new_arr:
    for k in range(3):
        result_arr=j[k:k+5]
        reversed_arr=result_arr[::-1]
        if result_arr==reversed_arr:
            count=count+1
print(count)
