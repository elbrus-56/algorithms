"""
Быстрая сортировка. 
Его используют чаще других алгоритмов.
Время работы оценивается как O(nlog(n))
Массив разделяется на две части по разные стороны от опорного элемента. В процессе сортировки элементы меньше опорного помещаются перед ним, а равные или большие — позади.
Наилучшая производительность достигается тогда, когда опорный элемент делит список примерно пополам

"""



# Быстрая сортировка с помощью рекурсии

# Вариант А

def quicksort(array):

    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([11, 3, -3, 1, -4]))


# Вариант B

def quickSort(array):
    if len(array) > 1:
        pivot = array.pop()
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in array:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return (quickSort(smlr_lst) + equal_lst + quickSort(grtr_lst))
    else:
        return array