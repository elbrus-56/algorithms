# Множества
"""
Множество должно уметь:
    - добавлять элемент
    - проверять элемент
    - удалять элемент

1. Добавление выполняется с помощью хэш-функции
2. Проверка осуществляется с помощью линейного поиска, 2х циклов
3. Удаление элемента можно выполнить следующий образом:
    найдем элемент, вместо него копируем последний элемент в списке, и удаляем последний элемент.
"""

# Свое множество

setsize = 10
myset = [[] for _ in range(setsize)]

def add(x):
    myset[x % setsize].append(x)


def find(x):
    for now in myset[x % setsize]:
        if x == now:
            return True
    return False

def delete(x):
    xlist = myset[x % setsize]
    for i in range(len(xlist)):
        if xlist[i] == x:
            xlist[i], xlist[len(xlist)-1] = xlist[len(xlist)-1], xlist[i]
            xlist.pop()
            return


# задача 1
"""
сложность O(N^2)
"""

def two_number_sum(nums,x):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == x:
                return nums[i], nums[j]
    return 0, 0


"""
сложность O(N)
"""


def two_number_sum_1(nums, x):
    set_nums = set(nums)
    for i in range(len(nums)):
        if (x - nums[i]) in set_nums:
            return nums[i], x - nums[i]
        set_nums.add(nums[i])
    return 0, 0

# Задача 2

def find_word(dictionary, text):
    goodwords = set(dictionary)

    for word in dictionary:
        for delpos in range(len(word)):
            goodwords.add(word[:delpos] + word[delpos+1:]) # всевозможные комбинации слов

    ans = []

    for word in text:
        ans.append(word in goodwords)
    return ans
