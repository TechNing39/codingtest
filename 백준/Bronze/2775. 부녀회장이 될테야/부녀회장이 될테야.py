T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    arr = []
    for i in range(n + 1):
        arr.append(i)

    for i in range(k):
        for j in range(1, n + 1):
            arr[j] = arr[j] + arr[j - 1]

    print(arr[n])