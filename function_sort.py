# Функция для поиска наименьшего значения

def find_smallest(arr):
    smallest = arr[0]
    # print(smallest)
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

#  Функция сортировки

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

arr = [11, 3, -3, 1, -4]
# print(selection_sort(arr))


# Быстрая сортировка с помощью рекурсии

def quicksort(array):

    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        print(pivot)
        less = [i for i in array[1:] if i <= pivot]
        print("less",less)
        greater = [i for i in array[1:] if i > pivot]
        print("gr",greater)

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([11, 3, -3, 1, -4]))