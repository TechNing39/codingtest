T=int(input())

for _ in range(T):
    R,S=input().split()
    R=int(R)
    result=[]

    for ch in S:
        for _ in range(R):
            result.append(ch)
    print(''.join(result))
