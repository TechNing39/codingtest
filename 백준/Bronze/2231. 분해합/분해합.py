N=int(input())
for i in range(1,N+1):
   S=map(int,list(str(i)))
   answer=i+sum(S)

   if answer==N:
    print(i)
    break
else:
    print(0)