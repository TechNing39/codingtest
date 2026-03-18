import math

num1,num2=map(int,input().split())

for i in range(num2,0,-1):
    if num1%i==0 and num2%i==0:
        print(i)
        break


b=num1*num2//math.gcd(num1,num2)
print(b)