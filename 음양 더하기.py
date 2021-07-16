def solution(absolutes, signs):

    answer = 0

    for sign in range(len(signs)):

        if signs[sign]:
            continue
        else:
            absolutes[sign] = -absolutes[sign]
    
    answer = sum(absolutes)
    return answer
