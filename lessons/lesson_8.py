# Генерация всех перестановок

def gen_numbers(N: int, M: int, prefix=None):
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        gen_numbers(N, M-1, prefix)
        prefix.pop()

# print(gen_numbers(4, 5))


def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
        return
    gen_bin(M-1, prefix+"0")
    gen_bin(M-1, prefix+"1")

# gen_bin(4)


def find(number, A):
    """
    Ищет number в A и возвращает True, если такой есть и False,
    если такого нет
    """
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
    return flag


def gen_permutations(N: int, M: int = -1, prefix=None):
    """
    Генерация всех перестановок N чисел в M позициях, с префиксом prefix
    """
    M = N if M == -1 else M  # по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        gen_permutations(N, M-1, prefix)
        prefix.pop()


print(gen_permutations(3))
