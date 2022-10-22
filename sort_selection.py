"""
1. За опорную точку берется первое значение массива, это значение сравнивается
 со всеми
остальными значениями этого массива и ищется максимум или мининимум.
2. Найденное значение меняется местами с первым элементом.
3. А дальше все заново с пункта 1.

Затраты времени на сортировку выборкой в среднем составляют O(n²)

"""

# Вариант 1


def selection_sort(nums):
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(nums)-1):
        # Исходно считаем наименьшим первый элемент
        smallest = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j
        # Самый маленький элемент меняем с первым в списке
        nums[i], nums[smallest] = nums[smallest], nums[i]


# Проверяем, что оно работает
random_list_of_nums = [12, 3, 13, 7, 20]

selection_sort(random_list_of_nums)
# print(random_list_of_nums)


# Вариант 2

def find_smallest(arr):
    smallest = arr[0]
    # print(smallest)
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


arr = [11, 3, -3, 1, -4]
# print(selection_sort(arr))
