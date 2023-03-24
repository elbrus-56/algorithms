# # Линейный поиск в массиве


# def array_search(A, N, x):
#     """
#     Поиск числа х в массиве А от 0 до N-1 включительно.
#     Возвращает индекс элемента х. Или -1 при отсутствии.
#     Если присутствует 2 и более одинаковых значений, то вернуть индекс
#      первого
#     """
#     for k in range(N):
#         if A[k] == x:
#             return k


# def test_array_search():
#     A1 = [1, 2, 3, 4, 5]
#     m = array_search(A1, 5, 4)
#     if m == 3:
#         print("#test - ok")
#     else:
#         print("#test - fail")


# test_array_search()


# # Инверсия списка

# def invert_array(A, N):
#     for k in range(N//2):
#         A[k], A[N-1-k] = A[N-1-k], A[k]


# def test_invert_array():
#     A1 = [1, 2, 3, 4, 5]
#     m = invert_array(A1, 5)
#     print(A1)
#     if A1 == [5, 4, 3, 2, 1]:
#         print("#test2 - ok")
#     else:
#         print("#test2 - fail")


# test_invert_array()


# # Циклический сдвиг в массиве Влево/Вправо

# def cycle_move_left(A, N):
#     tmp = A[0]
#     for k in range(N-1):
#         A[k] = A[k+1]
#     A[N-1] = tmp
#     return A


# def cycle_move_right(A, N):
#     tmp = A[N-1]
#     for k in range(N-1, 0, -1):
#         A[k] = A[k-1]
#     A[0] = tmp
#     return A


# def test_cycle_move():
#     A1 = [1, 2, 3, 4, 5]
#     m = cycle_move_left(A1, 5)
#     print(m)
#     if m == [2, 3, 4, 5, 1]:
#         print("#test3 - ok")
#     else:
#         print("#test3 - fail")

#     A2 = [1, 2, 3, 4, 5]
#     n = cycle_move_right(A2, 5)
#     print(n)
#     if n == [5, 1, 2, 3, 4]:
#         print("#test4 - ok")
#     else:
#         print("#test4 - fail")


# test_cycle_move()


# Решето Эратосфена - алгоритм нахождения всех простых чисел от 1 до n.

def sieve(N):
    A = [True] * N
    A[0] = A[1] = False
    for k in range(2, N):
        if A[k]:
            for m in range(2*k, N, k):
                A[m] = False
    for k in range(N):
        print(k, "-", "простое" if A[k] else "сложное")  # Тернарный оператор


sieve(1000000000)


# B = [0] * 5  # Создаем массив, с заданным количеством элементов
# # Уровень заполненности (Является индексом, в который нужно положить элемент)
# top = 0
# x = int(input())
# count = 0
# while count < len(B):
#     B[top] = x
#     top += 1
#     count += 1
#     x = int(input())
# print(B)
