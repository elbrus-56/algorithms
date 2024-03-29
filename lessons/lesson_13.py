# Стек или очередь LIFO
# Последний вошел, первый вышел
# push и pop - базовые операции
# size - узнать сколько всего сейчас
# top - 
# is_empty - проверка на пустоту


"""
Модуль описывающий струтуру данных - стек

>>> clear()
>>> is_empty()
True
>>> push(1)
>>> push(2)
>>> push(3)
>>> is_empty()
False
>>> pop()
3
>>> pop()
2
>>> pop()
1
>>> is_empty()
True

"""


_stack = []

def push(x):
    """
    Добавляет элемент х в конец стэка

    >>> size = len(_stack)
    >>> push(5)
    >>> len(_stack) - size
    1
    >>> _stack[-1]
    5

    """
    _stack.append(x)


def pop():
    x = _stack.pop()
    return x

def clear():
    _stack.clear()


def is_empty():
    return len(_stack) == 0


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()