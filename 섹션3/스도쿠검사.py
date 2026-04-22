arr=[]
check=[]
ch1=True
ch2=True
ch3=True

result=[]
def Check(check):
    if check=={1,2,3,4,5,6,7,8,9}:
        return True
    else:
        return False

for _ in range(9):
    arr.append(list(map(int,input().split())))

for i in range(9):
    for j in range(9):
        check.append(arr[i][j])
    ch1=Check(set(check))
    check=[]
    result.append(ch1)

if result==[True,True,True,True,True,True,True,True,True]:
    ch1=True
else:
    ch1=False

result=[]
for k in range(9):
    for l in range(9):
        check.append(arr[l][k])
    ch2=Check(set(check))
    check=[]
    result.append(ch2)
if result==[True,True,True,True,True,True,True,True,True]:
    ch2=True
else:
    ch2=False

result=[]
for m in range(3):
    for n in range(3):
        for o in range(3):
            for p in range(3):
                check.append(arr[o+3*n][p+3*m])
        ch3=Check(set(check))
        check=[]
        result.append(ch3)
if result==[True,True,True,True,True,True,True,True,True]:
    ch3=True
else:
    ch3=False

if ch1 and ch2 and ch3:
    print('YES')
else:
    print('NO')
