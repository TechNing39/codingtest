num=int(input())
num_arr=[]
arr=[]
count=0
for _ in range(num-2):
    arr.append(0)

num_arr.append(arr)
for _ in range(num):
    num_arr.append(list(map(int,input().split())))
num_arr.append(arr)

for k in num_arr:
    k.append(0)
    k.insert(0,0)

for j in range(num):
    for i in range(num):
        if( (num_arr[i+1][j+1]>num_arr[i+2][j+1])and
        (num_arr[i+1][j+1]>num_arr[i][j+1])and
        (num_arr[i+1][j+1]>num_arr[i+1][j+2])and
        (num_arr[i+1][j+1]>num_arr[i+1][j])):
            count=count+1
print(count)
