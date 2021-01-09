def solution(array, commands):
    answer = []

    for x,y,z in commands:
        slice_array=array[x-1:y]
        
        sort_slice_array=sorted(slice_array)
        """
        slice_array=slice_array.sort()
        sort_slice_array=slice_array
        """
        answer.append(sort_slice_array[z-1])
    
    return answer

array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array,commands))