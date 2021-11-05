# def sum_in_list(search_sum, sorted_list):
#     #  bruteforce 형식으로 해결
#     for i in range(len(sorted_list)):
#         for j in range(i + 1, len(sorted_list)):
#             if sorted_list[i] + sorted_list[j] == search_sum:
#                 return True
#     return False
# def sum_in_list(search_sum, sorted_list):
#     for i in sorted_list:
#         if search_sum - i in sorted_list:
#             return True
#     return False
def sum_in_list(search_sum, sorted_list):
    row = 0
    high = len(sorted_list) - 1

    for i in range(len(sorted_list)):
        if sorted_list[row] + sorted_list[high] == search_sum:
            return True
        elif sorted_list[row] + sorted_list[high] > search_sum:
            high -= 1
        elif sorted_list[row] + sorted_list[high] < search_sum:
            row += 1
    return False


test_list = [1, 2, 5, 6, 7, 9, 11]
print(sum_in_list(15, test_list))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))