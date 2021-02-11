def solution(n):
    answer=0
    n=str(n)
    arr=list(n)
    for i in range(len(n)):
        answer=answer+int(arr[i])
    return answer
