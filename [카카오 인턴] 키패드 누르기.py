def solution(numbers, hand):
    answer = ''
    L_check = [3,0]
    R_check = [3,2]
    left_answer = [1,4,7]
    right_answer = [3,6,9]
    keypad = {
        1:[0,0],
        2:[0,1],
        3:[0,2],
        4:[1,0],
        5:[1,1],
        6:[1,2],
        7:[2,0],
        8:[2,1],
        9:[2,2],
        0:[3,1]
        }
    
    for number in numbers:
        if number in left_answer:
            answer += 'L'
            L_check = keypad[number]

        elif number in right_answer:
            answer += 'R'
            R_check = keypad[number]
        
        else:
            if (abs(L_check[0] - keypad[number][0])) + (abs(L_check[1] - keypad[number][1])) > abs(R_check[0] - keypad[number][0]) + abs(R_check[1] - keypad[number][1]):
                answer += 'R'
                R_check = keypad[number]
            elif abs(L_check[0] - keypad[number][0]) + abs(L_check[1] - keypad[number][1]) < abs(R_check[0] - keypad[number][0]) + abs(R_check[1] - keypad[number][1]):
                answer += 'L'
                L_check = keypad[number]
            else:
                if hand == 'left':
                    answer += 'L'
                    L_check = keypad[number]
                else:
                    answer += 'R'
                    R_check = keypad[number]

    return answer

print(solution(	[1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))