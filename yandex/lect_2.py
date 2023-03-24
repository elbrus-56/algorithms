# Линейный поиск - способ поиска, когда перебираются все элементы, сложность O(N)

        # Однопроходный алгоритм

# Задача 1

"""
Найти первое левое вхождение числа в пследовательность
"""


def find_x(seq, x):
    ans = -1 # индикатор, что число не встречалось ранее
    for i in range(len(seq)):
        if ans == -1 and seq[i] == x:
            ans = i
    return ans


# Задача 2

"""
Найти первое правое вхождение числа в пследовательность.
Можно также начать итерацию с обратной стороны и свести к первой задаче
"""


def find_x(seq, x):
    ans = -1  # индикатор, что число не встречалось ранее
    for i in range(len(seq)):
        if seq[i] == x:
            ans = i
    return ans


# Задача 3

"""
Поиск максимума в последовательности
Решение - сравнивать значения относитель нулевого элемента
"""


def find_x(seq):
    ans = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > ans:
            ans = seq[i]
    return ans


def find_x(seq):
    ans = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[ans]:
            ans = i
    return seq[ans]


# Задача 4

"""
Поиск двух максимумов

В зависимости от условия в последовательности [3,1,2,3] могут быть такие варианты: либо два максимума -
это 3 и 3, либо 3 и 2

Решение:

max_1 и max_2 - это первые 2 элемента последовательности

Начинаем итерироваться

Возникает 3 варианта:

1. Если новое число больше max_1 и max_2
2. Если новое число находится между max_1 и max_2
3. Если новое число меньше max_1 и max_2

"""

def find_max(seq):
    max_1 = max(seq[0], seq[1])
    max_2 = min(seq[0], seq[1])

    for i in range(2, len(seq)):
        if seq[i] > max_1:
            max_2 = max_1
            max_1 = seq[i]

        elif seq[i] > max_2:
            max_2 = seq[i]

    return max_1, max_2


# Задача 5

"""
найти наименьшее четное число
флаг нужен, для экономии

"""


def find_min(seq):
    ans = -1
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (ans == -1 or seq[i] > ans):
            ans = seq[i]
    return ans


def find_min(seq):
    flag = False
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (not flag or seq[i] > ans):
            ans = seq[i]
            flag = True
    return ans



        # Двухпроходные алгоритмы


# Задача 6
"""
Дана последовательность слов. Вывести все самые короткие слова
"""

def short_words(words):
    minlen = len(words[0])
    for word in words:
        if len(word) < minlen:
            minlen = len(word)

    ans = []

    for word in words:
        if len(word) == minlen:
            ans.append(word)

    return ' '.join(ans)


# Задача 7
"""
PitCraft
"""

def isleflood(h):
    # Находим максимум
    maxpos = 0
    for i in range(len(h)):
        if h[i] > h[maxpos]:
            maxpos = i

    #
    ans = 0
    nowm = 0


    for i in range(maxpos):
        if h[i] > nowm:
            nowm = h[i]

        ans += nowm - h[i]

    nowm = 0

    for i in range(len(h)-1, maxpos, -1):
        if h[i] > nowm:
            nowm = h[i]

        ans += nowm - h[i]

    return ans


# Задача 8 RLE

"""
Подсчитать количество символов в строке
"""

# Задача 1 простая, сведение строки к символу

def count_var(s):
    lastsym = s[0]
    ans = []

    for i in range(1, len(s)):
        if s[i] != lastsym:
            ans.append(lastsym)
            lastsym = s[i]

    ans.append(lastsym)

    return " ".join(ans)


# Задача 2 сведение строки с подсчетом символов


def RLE(s):
    def pack(s, cnt):
        if cnt > 1:
            s + str(cnt)
        return s

    lastsym = s[0]
    lastpos = 0

    ans = []

    for i in range(len(s)):
        if s[i] != lastsym:
            ans.append(pack(lastsym, i-lastpos))
            lastpos = i
            lastsym = s[i]

    ans.append(pack(s[lastpos],len(s)-lastpos))

    return "".join(ans)
