"""
현재 상황은 어피치가 화살 n발을 다 쏜 후이고 라이언이 화살을 쏠 차례입니다.
라이언은 어피치를 가장 큰 점수 차이로 이기기 위해서 n발의 화살을 어떤 과녁 점수에 맞혀야 하는지를 구하려고 합니다.

화살의 개수를 담은 자연수 n, 어피치가 맞힌 과녁 점수의 개수를 10점부터 0점까지 순서대로 담은 정수 배열 info 가
매개변수로 주어집니다. 이때, 라이언이 가장 큰 점수 차이로 우승하기 위해 n발의 화살을 어떤 과녁 점수에 맞혀야 하는지를
10점부터 0점까지 순서대로 정수 배열에 담아 return 하도록 solution 함수를 완성해 주세요. 만약, 라이언이 우승할 수 없는
경우(무조건 지거나 비기는 경우)는 [-1]을 return 해주세요.
"""
import itertools


def ryan_shot(n):
    shot_permutation = list(itertools.product([i for i in range(1, 11)], repeat=n))
    return shot_permutation


def list_sort_permutation(shot_permutation, info):
    answer = [0 for i in range(11)]
    apeach_point = 0
    ryan_point = 0
    for i in range(len(shot_permutation)):
        for j in range(5):
            answer[shot_permutation[i][j]] += 1
        answer.reverse()
        for z in range(len(info)):
            if (info[z] != 0 or answer[z] != 0) and info[z] >= answer[z]:
                apeach_point += (10 - z)
            elif info[z] < answer[z]:
                ryan_point += (10 - z)

        if ryan_point > apeach_point:
            break
        if apeach_point >= ryan_point:
            answer = [0 for i in range(11)]
            apeach_point = 0
            ryan_point = 0
        else:
            break
    print(apeach_point)
    print(ryan_point)
    return answer


def solution(n, info):
    shot_permutation = ryan_shot(n)
    answer = list_sort_permutation(shot_permutation, info)
    return answer


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))

