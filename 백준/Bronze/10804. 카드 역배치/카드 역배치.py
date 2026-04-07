card=[]
reversed_card=[]

for i in range(1,21):
    card.append(i)
    
for j in range(1,11):
    a,b=map(int,input().split())
    reversed_card=card[a-1:b]
    reversed_card=reversed_card[::-1]
    l=0
    for k in range(a-1,b):
        card[k]=reversed_card[l]
        l+=1
print(*card)

