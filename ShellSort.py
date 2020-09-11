from numpy import random


def shell_sort(data):
    sublist_count = len(data) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(data, start_position, sublist_count)
        sublist_count = sublist_count // 2
    return data


def gap_insertion_sort(input_list, start, gap):
    for i in range(start + gap, len(input_list), gap):
        current_value = input_list[i]
        position = i
        while position >= gap and input_list[position - gap] > current_value:
            input_list[position] = input_list[position - gap]
            position = position - gap
        input_list[position] = current_value


x = random.rand(random.randint(5, 15)) * 100
print("Unsorted array: " + str(x))
print("Sorted array:" + str(shell_sort(x)))