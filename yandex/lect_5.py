# Префиксные суммы

"""
prefixsum должен быть на единицу больше nums

"""

def make_prefix_sum(nums):
    prefixsum = [0] * (len(nums) + 1) # создаем массив с длинной на один больше
    for i in range(1, len(nums) + 1): # Начинае итерацию с 1, потому что в массиве первым уже лежит 0
        prefixsum[i] = prefixsum[i-1] + nums[i-1] # считаем сумму предыдущей суммы и предыдущего числа
    return prefixsum

def rsq(prefixsum, l, r):
    return prefixsum[r] - prefixsum[l]


# Задача подсчитать количество нулей в последовательности
# Стандартный метод = перебор
# РЕализиция с помощью префиксной суммы


def make_prefix_sum(nums):

    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        if nums[i - 1] == 0:
            prefixsum[i] = prefixsum[i-1] + 1
        else:
            prefixsum[i] = prefixsum[i-1]
    return prefixsum


def rsq(prefixsum, l, r):
    return prefixsum[r] - prefixsum[l]


# Дана послед-ть чисел длиной N. Найти количество отрезков с нулевой суммой

# 1 способ N^3

def f1(nums):
    cntranges = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            rangesum = 0
            for k in range(i, j):
                rangesum += nums[k]
            if rangesum == 0:
                cntranges += 1
    return cntranges


# print(f1([1, 2, -1, 3, 4, -2, 5, -3]))

# 2 способ


def f2(nums):
    cntranges = 0
    for i in range(len(nums)):
        rangesum = 0
        for j in range(i, len(nums)):
            rangesum += nums[j]
            if rangesum == 0:
                cntranges += 1
    return cntranges


# print(f2([1, 2, -1, 3, 4, -2, 5, -3]))


#3 способ O^N

def count_prefix_sum(nums):
    prefixsumbyvalue = { 0 : 1}
    nowsum = 0
    for now in nums:
        nowsum += now
        if nowsum not in prefixsumbyvalue:
            prefixsumbyvalue[nowsum] = 0
        prefixsumbyvalue[nowsum] += 1
    return prefixsumbyvalue


def count_some_ranges(prefixsumbyvalue):
    countranges = 0
    for nowsum in prefixsumbyvalue:
        cntsum = prefixsumbyvalue[nowsum]
        print(cntsum, cntsum-1)
        countranges += cntsum * (cntsum - 1) // 2
    return countranges


print(count_some_ranges(count_prefix_sum([1, 2, -1, 3, 4, -2, 5, -3])))
