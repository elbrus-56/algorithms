# мультимножество (хэш-таблица)

setsize = 10

myset = [[] for _ in range(setsize)]

def add(x):
    myset[x % setsize].append(x)

def find(x):
    for now in myset[x % setsize]:
        if now == x:
            return True
    return False

def delete(x):
    xlist = myset[x % setsize]
    for i in range(len(xlist)):
        if xlist[i] == x:
            xlist[i], xlist[len(xlist) - 1] == xlist[len(xlist) - 1], xlist[i]
            xlist.pop()
    return


# Поиск суммы двух чисел

def twotermswithsumit(nums, x):
    prevnums = set()
    for i in nums:
        if x - i in prevnums:
            return i, x - i
        prevnums.add(i)
    return 0, 0


print(twotermswithsumit([2, 33, 4, 5, 3, 1, 3,
      5, 6, 7, 8, 9, 0, 1, 2, 3, 44, 3, 3], 2))
