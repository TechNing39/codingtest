L = int(input())
s = input()

r = 31
M = 1234567891
total_hash = 0

for i in range(L):
    num = ord(s[i]) - ord('a') + 1
    total_hash = (total_hash + num * (r ** i)) % M

print(total_hash)