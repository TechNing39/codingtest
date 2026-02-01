sentence=list(input())
cnt=0
for x in sentence:
    if(x==' '):
        cnt=cnt+1
if(sentence[0]==' '):
    cnt=cnt-1
if(sentence[-1]==' '):
    cnt=cnt-1
print(cnt+1)