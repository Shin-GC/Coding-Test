def course_selection(course_list):
    # 코드를 작성하세요.
    course_list.sort(key=lambda c: c[1])  # 튜플을 두번째 원소를 기준으로 오름차 순 정리 [중요!]

    registration_list = [course_list[0]]
    check = 0
    for i in range(len(course_list)):
        if registration_list[check][1] != course_list[i][1] and registration_list[check][1] < course_list[i][0]:
            registration_list.append(course_list[i])
            check += 1

    return registration_list


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))

