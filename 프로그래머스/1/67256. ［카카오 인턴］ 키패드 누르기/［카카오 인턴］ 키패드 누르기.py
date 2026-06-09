def solution(numbers, hand):
    keypad={
        1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
    '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    left_pos=keypad['*']
    right_pos=keypad['#']
    answer = ''
    for num in numbers:
        if num==1 or num==4 or num==7:
            answer += 'L'
            left_pos=keypad[num]
        elif num==3 or num==6 or num==9:
            answer += 'R'
            right_pos=keypad[num]
        else:
            x,y=keypad[num]
            left_abs = abs(left_pos[0] - x) + abs(left_pos[1] - y)
            right_abs = abs(right_pos[0] - x) + abs(right_pos[1] - y)
            if left_abs>right_abs:
                answer += 'R'
                right_pos = keypad[num]
            elif left_abs<right_abs:
                answer += 'L'
                left_pos = keypad[num]
            else:
                if hand=="right":
                    answer += 'R'
                    right_pos = keypad[num]
                else:
                    answer += 'L'
                    left_pos = keypad[num]
    return answer