# Реализация бинарного поиска в массиве
# Поиск осуществляется с помощью введения условных границ. Тем самым, мы
# можем найти несколько элементов в списке.
# Работает только в отсортированном списке. Сложность O(log n)

def left_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right


my_list = [1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("от", left_bound(my_list, 15), "до", right_bound(my_list, 15))


# Динамическое программирование

# Числа Фибоначчи
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


n = 4

fib = [0, 1] + [0] * (n-1)
for i in range(2, n+1):
    fib[i] = fib[i-1] + fib[i-2]

print(fib[i])

# Двумерные массивы

M = 3
N = 5
A = [[0]*M for i in range(N)]

print(A)

B = [[0]*M] * N  # Неверная запись

print(B)
