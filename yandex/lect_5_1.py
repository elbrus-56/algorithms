# 2 указателя
"""
Общий подход - левый указатель двигаем на единицу вперед
Правый указатель - двигаем от текущей позиции
"""
# O^N подсчитать количество пар больше 4х

def cntpair(sortednums, k):
    countpairs = 0
    last = 0
    for first in range(len(sortednums)):

        while last < len(sortednums) and sortednums[last] - sortednums[first] <= k:
            print(last, sortednums[last], sortednums[first])
            last += 1
        countpairs += len(sortednums) - last
    return countpairs


print(cntpair([1, 3, 5, 7, 8], 4))


# Метод O^N2
# Двойной цикл и сранение каждого значения с каждым
