
T = int(input())

for test_case in range(1, T + 1):

    str1 = input()
    str2 = input()

    count = {}

    for ch in str2:

        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    max_count = 0

    for ch in str1:

        if ch in count:

            if count[ch] > max_count:
                max_count = count[ch]

    print(f"#{test_case} {max_count}")