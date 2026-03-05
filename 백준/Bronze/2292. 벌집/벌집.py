N=int(input())

last_number=1
count=1

while N>last_number:
    last_number+=6*count
    count+=1
print(count)
