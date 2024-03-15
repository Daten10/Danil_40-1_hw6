# Пузырьковая сортировка
list_of_numbers1 = [1, 34, 6, 765, 54, 3, 2, 100]
list_of_numbers2 = [2, 35, 16, 76, 54, 73, 1, 234]


def bubble_sort(list_of_numbers):
    for i in range(list_of_numbers[0], list_of_numbers[-1]):
        for j in range(0, len(list_of_numbers) - i - 1):
            if list_of_numbers[j] > list_of_numbers[j+1]:
                tmp = list_of_numbers[j]
                list_of_numbers[j] = list_of_numbers[j+1]
                list_of_numbers[j+1] = tmp
    print('Bubble Sort:')
    return list_of_numbers


print(bubble_sort(list_of_numbers1))


# Сортировка выбором

def selection_sort(list_of_numbers):
    for i in range(len(list_of_numbers) - 1):
        min_pos = i
        for j in range(i + 1, len(list_of_numbers)):
            if list_of_numbers[j] < list_of_numbers[min_pos]:
                min_pos = j
        list_of_numbers[i], list_of_numbers[min_pos] = list_of_numbers[min_pos], list_of_numbers[i]
    print('Selection Sort:')
    return list_of_numbers


print(selection_sort(list_of_numbers2))


# Бинарный поиск


def binary_search(val, srt_list):
    n = len(srt_list)
    result_ok = False
    first = 0
    last = n - 1
    pos = -1
    while first <= last:
        middle = (first + last) // 2
        if val == srt_list[middle]:
            result_ok = True
            pos = middle
            break
        elif val > srt_list[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if result_ok:
        print(f'element {val} found!')
        print('position index is', pos)
    else:
        print('element not found!')


sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20]
binary_search(11, sorted_list)

