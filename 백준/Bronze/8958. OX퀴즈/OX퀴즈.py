T = int(input())

for _ in range(T):
    score = input()
    streak = 0
    total = 0

    for ch in score:
        if ch == 'O':
            streak += 1
            total += streak
        else:
            streak = 0

    print(total)
