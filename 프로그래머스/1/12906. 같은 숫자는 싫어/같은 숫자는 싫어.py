def solution(arr):
    answer=[]
    answer.append(arr[0])
    print(answer)
    for x in arr:
        if answer[-1]!=x:
            answer.append(x)
    return answer