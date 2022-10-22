"""
Сортировка пузырьком, затраты времени оценивается как O(n2).
Суть в том, что первый элемент сравнивается со вторым. Если условие выполняется,
то элементы меняются местами и дальше 2ой эл-т сравнивается с 3-им и тд до конца списка.
Последний элемент сравнивать не нужно, поэтому длина списка len() - 1

"""


lst = [9,8,7,6,5,4,3,2,1]

for n in range(len(lst)-1):
    for i in range(len(lst)-1-n):
        print(lst[n], lst[i])
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
print(lst)


i = 0
while i < len(L):
    j = 0
    # print(L)
    while j < len(L)-1:
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]

        j += 1
    i += 1
    # print(L)
print(L)
