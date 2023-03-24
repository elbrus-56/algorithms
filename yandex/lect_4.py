# Словари и сортировка подсчётом
"""
Сортировку подсчетом неразумо использовать, если данные сильно разряжены.
(Пример, дано 10 значений из 1 млн или 1 млрд). Лучше использовать словарь

"""

def count_sort(seq):
    minval = min(seq)
    maxval = max(seq)

    k = (maxval - minval + 1)
    count = [0] * k

    for now in seq:
        count[now - minval] += 1

    nowpos = 0

    for val in range(0, k):
        for i in range(count[val]):
            seq[nowpos] = val + minval

            nowpos += 1

    return seq

# print(count_sort([5,5,2,3,1,5]))


# Задача 1

"""
Можно ли из числа А получить число Б

1. С помощью перестановки перебрать варианты числа А и сравнить с числом Б
2. Посчитать количество цифр в А и Б и сравнить
"""

def isdigit_permutatinos(x ,y):
    def count_digits(num):
        digits_count = [0] * 10

        while num > 0:
            lastdigit = num % 10
            digits_count[lastdigit] += 1
            num //= 10

        return digits_count

    digitsx = count_digits(x)
    digitsy = count_digits(y)
    for digit in range(10):
        if digitsx[digit] != digitsy[digit]:
            return False
    return True

# print(isdigit_permutatinos(1202, 2120))


# Задача 2

"""
Найти сколько пар ладей на поле бьет друг друга

С ферзями координата i-j, i+j . 4 словаря нужно.


"""

def countingbeatingrooks(rookcoords):
    def addrook(roworcol, key):
        if key not in roworcol:
            roworcol[key] = 0
        roworcol[key] += 1

    def countpairs(roworcol):
        pairs = 0
        for key in roworcol:
            pairs += roworcol[key] - 1

        return pairs

    rooksinrow = {}
    rooksincol = {}

    for row, col in rookcoords:
        addrook(rooksinrow, row)
        addrook(rooksincol, col)

    return countpairs(rooksinrow) + countpairs(rooksincol)


# print(countingbeatingrooks([[1, 3],[5, 3], [1,1], [4,1]]))


# Задача 3

"""
Вывести гистограмму, сложность О(N^2)
"""

def printchart(s):
    symcount = {}
    maxsymcount = 0

    for sym in s:
        if sym not in symcount:
            symcount[sym] = 0
        symcount[sym] += 1

        maxsymcount = max(maxsymcount, symcount[sym])

    sorted_uniq_syms = sorted(symcount.keys())

    for row in range(maxsymcount, 0, -1):
        for sym in sorted_uniq_syms:
            if symcount[sym] >= row:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(''.join(sorted_uniq_syms))


# printchart('Hello world!&')


# Задача 4
"""
Сгруппировать слова по общим буквам
input_sample = ["eat", "tea", "aet", "tan", "nat", "bat"]
output_sample = [["eat", "tea", "aet"],["tan", "nat"], ["bat"]]

"""

def groups_words(s):
    groups = {}

    for word in s:
        sortedword = ''.join(sorted(word))
        if sortedword not in groups:
            groups[sortedword] = []
        groups[sortedword].append(word)
    ans = []

    for sortedword in groups:
        ans.append(groups[sortedword])
    return ans


print(groups_words(["eat", "tea", "aet", "tan", "nat", "bat"]))
