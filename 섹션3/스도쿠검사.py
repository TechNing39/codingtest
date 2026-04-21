s_arr=[]
b_arr=[]
p=0
h=0
for _ in range(9):
    s_arr.append(list(map(int,input().split())))

for k in range(3):
    for i in range(3):
        for j in range(3):
            b_arr.append(s_arr[p][h])
            h=h+1

        h=0
        if p<8:
            p=p+1
p=0
h=3
for k in range(3):
    for i in range(3):
        for j in range(3):
            b_arr.append(s_arr[p][h])
            h=h+1

        h=3
        if p<8:
            p=p+1

p=0
h=6
for k in range(3):
    for i in range(3):
        for j in range(3):
            b_arr.append(s_arr[p][h])
            h=h+1

        h=6
        if p<8:
            p=p+1



if len(set(b_arr))==9:
    print('YES')
else:
    print('NO')
