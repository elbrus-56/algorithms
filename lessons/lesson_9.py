# Сортировка  слиянием
# Слияние отсортированных массивов в один

"""
Сортировка называется устойчивой, если она не меняет порядок равных элементов
"""

# def merge(A:list, B:list):
#     C = [0] * (len(A) + len(B))
#     i = k = n = 0
#     while i < len(A) and k < len(B):
#         if A[i] <= B[k]:
#             C[n] = A[i]
#             i += 1
#             n += 1
#         else:
#             C[n] = B[k]
#             k += 1
#             n += 1
#     while i < len(A):
#         C[n] = A[i]
#         i += 1
#         n += 1
#     while k < len(B):
#         C[n] = A[k]
#         k += 1
#         n += 1
#     return C

# print(merge([2,4,9], [1,4,6,8]))


def merge_1(A: list, B: list):
    C = []
    i = k = 0
    while i < len(A) and k < len(B):
        if A[i] < B[k]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[k])
            k += 1
    while i < len(A):
        C.append(A[i])
        i += 1
    while k < len(B):
        C.append(B[k])
        k += 1
    return C


print(merge_1([2, 4, 9], [4, 6, 8]))


# Сортировка слиянием с помощью рекурсии

# def merge_sort(A):
#     if len(A) <= 1:
#         return A
#     middle = len(A) // 2
#     L = [A[i] for i in range(0, middle)]
#     R = [A[i] for i in range(middle, len(A))]
#     merge_sort(L)
#     merge_sort(R)
#     C = merge(L,R)
#     for i in range(len(A)):
#         A[i] = C[i]
#     return C

# print(merge_sort([4,2,5,6,6,3,9,7]))


def merge_sort_1(A):
    if len(A) <= 1:
        return A
    middle = len(A) // 2
    L = merge_sort_1(A[0:middle])
    R = merge_sort_1(A[middle:])
    return merge_1(L, R)


print(merge_sort_1([4, 2, 5, 6, 6, 3, 9, 7]))


# Быстрая сортировка Тони Хоара

def quick_sort(A):
    if len(A) <= 1:
        return
    bar = A[0]
    L = []
    M = []
    R = []

    for x in A:
        if x == A[0]:
            M.append(x)
        elif x < A[0]:
            L.append(x)
        else:
            R.append(x)
    quick_sort(L)
    quick_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1
    return A


print(quick_sort([4, 2, 5, 6, 6, 3, 9, 7]))


# Проверка списка на отсортированность за время О(n)

def check_sort(A, ascending=False):
    flag = True
    s = 2*int(ascending)-1
    for i in range(0, len(A)-1):
        if s*A[i] < s*A[i+1]:
            flag = False
            break
    return flag


print(check_sort([1, 2, 3, 4, 5]))
