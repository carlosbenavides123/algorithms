# given a array, and a pivot index int
# partition the array s.t. all it is sorted around the pivot
# arr = [0, 1, 2, 0, 2, 1, 1] pivot = 3
# res = [0, 0, 1, 2, 2, 1, 1]; arr[3] is 0
# arr = [0, 1, 2, 0, 2, 1, 1] pivot = 2
# res = [0, 1, 0, 1, 1, 2, 2]; arr[2] is 2

# def dutch_flag(arr, pivot):
#     num = arr[pivot]
#     smaller = 0
#     print(num)
#     for i in range(len(arr)):
#         curr_num = arr[i]
#         if curr_num < num:
#             arr[i], arr[smaller] = arr[smaller], arr[i]
#             smaller += 1
#     higher = len(arr) - 1
#     for i in reversed(range(len(arr))):
#         curr_num = arr[i]
#         if curr_num > num:
#             arr[i], arr[higher] = arr[higher], arr[i]
#             higher -= 1
#     return arr

def dutch_flag(arr, pivot):
    smaller, equal = 0, 0
    larger = len(arr)
    num = arr[pivot]

    while equal < larger:
        curr_num = arr[equal]
        if curr_num < num:
            arr[equal], arr[smaller] = arr[smaller], arr[equal]
            smaller += 1
            equal += 1
        elif curr_num == num:
            equal += 1
        else:
            larger -= 1
            arr[equal], arr[larger] = arr[larger], arr[equal]
    return arr    

print(dutch_flag([0, 1, 2, 0, 2, 1, 1],2))
print(dutch_flag([0, 1, 2, 0, 2, 1, 1],3))
print(dutch_flag([0, 1, 2, 0, 2, 1, 1],1))

    

