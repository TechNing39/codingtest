A,B=input().split()
A_reversed=A[::-1]
B_reversed=B[::-1]

A_reversed=int(A_reversed)
B_reversed=int(B_reversed)

result=[]
result.append(A_reversed)
result.append(B_reversed)
print(max(result))