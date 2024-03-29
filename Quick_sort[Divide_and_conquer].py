# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    p = end
    b = start  # pivot 보다 값이 낮을경우 위치를 변경하고 b 값 1 증가
    for i in range(start, end):
        if my_list[i] < my_list[p]:  # small 그룹이기 때문에 현재 b 인덱스와 위치를 교환한 후 b 와 i 모두 값 증가
            swap_elements(my_list, i, b)
            i += 1
            b += 1
        i += 1
    swap_elements(my_list, b, p)
    p = b
    return p


# 퀵 정렬
def quicksort(my_list, start=0, end=None):
    # 코드를 작성하세요.
    if end is None:
        end = len(my_list) - 1
    if end - start < 1:
        return
    pivot = partition(my_list, start, end)
    quicksort(my_list, start, pivot - 1)
    quicksort(my_list, pivot + 1, end)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1)  # start, end 파라미터 없이 호출
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2)  # start, end 파라미터 없이 호출
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3)  # start, end 파라미터 없이 호출
print(list3)