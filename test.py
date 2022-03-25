"""
from pygost import gost34112012512
print('Привет'.encode("utf-8"))
data_for_signing = 'hello'.encode("utf-8")
dgst = gost34112012512.new(data_for_signing).hexdigest()
print(dgst)
"""

# b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
# b'\xd1\x82\xd0\xb5\xd0\xb2\xd0\xb8\xd1\x80\xd0\x9f'
# 82d1b5d0b2d0b8d080d19fd0
# d182d0b5d0b2d0b8d180d09f
def qsort(num_list:list) -> list:

    if len(num_list) < 1:
        return num_list
    mid = num_list[len(num_list) // 2]
    left_list = []
    right_list = []
    for i in range(len(num_list)):
        if num_list[i] < mid:
            left_list.append(num_list[i])
        if num_list[i] > mid:
            right_list.append(num_list[i])
    return qsort(left_list) + [mid]*num_list.count(mid) + qsort(right_list)

def selection_sort(num_list:list) -> list:
    for i in range(len(num_list)):
        min = i
        for j in range(i+1,len(num_list)):
            if num_list[j] < num_list[min]:
                min = j
        num_list[min],num_list[i] = num_list[i],num_list[min]

    return num_list

test = [9,4,2,6,8,0,5,3,76,8,5,3,7,0,8,5,2,9,1,2,3,4,5,6,7]
test2 = [9,4,2,6,8,0,5,3,76,8,5,3,7,0,8,5,2,9,1,2,3,4,5,6,7]
print(selection_sort(test))
print(qsort(test))