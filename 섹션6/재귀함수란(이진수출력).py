n = int(input())

def number(x):
    if x == 0:
        return
    number(x // 2)
    print(x % 2, end='')

number(n)
