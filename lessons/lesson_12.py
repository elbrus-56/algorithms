# Алгоритм Левенштейна

"""
A = "колокол"
B = "молоко" 

Действия, которые допустимы, чтобы слово А стало словом B:
1. Замена
2. Вставка
3. Удаление

F(ij) - минимальное редакционное расстояние между срезами A[0:i] и B[0:j]

O(m * n)
"""


def lev(A, B):
    F = [[(i+j) if i*j == 0 else 0 for j in range(len(B)+1)] 
        for i in range(len(A)+1)]

    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = 1 + min(F[i-1][j], F[i][j-1], F[i-1][j-1])
    return F[len(A)][len(B)]


print(lev("дом", "паром"))


# Алгоритм Левенштейна

def distance(a, b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n, m)) space
        a, b = b, a
        n, m = m, n

    current_row = range(n + 1)  # Keep current and previous row, not entire matrix
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


print(distance("текст", "тест"))



# Проверка равенства строк
"""
Как вариант можно использовать алгоритм Левенштейна, есди ред. расстояние равно 0, значит строки равны.
Но можно использовать наивный алгоритм с меньшей сложностью.
"""

# Наивный алгоритм (A == B)


def equal(A, B):
    if len(A) != len(B): # Проверка длины
        return False
    for i in range(len(A)): # Проверка символов
        if A[i] != B[i]:
            return False
    return True


# Поиск подстроки в строке

# Наивный метод

def search(s, sub):
    for i in range(0, len(s)-len(sub)):
        if equal(s[i, i+len(sub)], sub):
            print(i)


# Префикс-функция O(N+M)
"""
Функция для поиска наибольшего префикса
"""
def prefix_function(input_string: str) -> list:
   
    # list for the result values
    prefix_result = [0] * len(input_string)

    for i in range(1, len(input_string)):

        # use last results for better performance - dynamic programming
        j = prefix_result[i - 1]
        while j > 0 and input_string[i] != input_string[j]:
            j = prefix_result[j - 1]

        if input_string[i] == input_string[j]:
            j += 1
        prefix_result[i] = j

    return prefix_result

print(prefix_function("abcdaabоc"))


def longest_prefix(input_str: str) -> int:
    """
    Prefix-function use case
    Finding longest prefix which is suffix as well
    >>> longest_prefix("aabcdaabc")
    4
    >>> longest_prefix("asdasdad")
    4
    >>> longest_prefix("abcab")
    2
    """

    # just returning maximum value of the array gives us answer
    return max(prefix_function(input_str))


    # Алгоритм Кнута-Морриса-Пратта O(N + M)

def kmp(text: str, sub: str) -> list:
    sub_len = len(sub)
    text_len = len(text)
    print(text_len, sub_len)
    if not text_len or sub_len > text_len:
        return []
    P = prefix_function(sub)
    print(">>>", P)
    entries = []
    i = j = 0
    while i < text_len:
        if text[i] == sub[j]:
            # print(j, i)
            if j == sub_len - 1:
                entries.append(i - sub_len + 1)
                j = P[j]
            else:
                j += 1
            i += 1
        # text[i] 1= sub[j]
        elif j:     # j > 0
            j = P[j-1]
        else:
            i += 1
    return entries


print(kmp("лилилось лилилась", "лилила"))