# Функция, демонстрирующая бинарный поиск
# Подходит только для сортированных списков

"""
Бинарный поиск
В отличии от простого поиска, при бинарном каждый раз исключается половина списка. В общем случае для списка из n 
элементов бинарный поиск выполняется за log2n шагов, тогда как простой выполнится за n шагов.
Бинарный поиск работает только в отсортированном списке.

"""


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = round((low + high)/2)
        guess = list[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


my_list = [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
print("Индекс =", binary_search(my_list, 1))