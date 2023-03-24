# Связные списки

# a = [1]
# a.append([2])
# a[1].append([3,None])
# a = [0,a]
# a = [-1, a]
# print(a)


# p = a
# while p is not None:
#     print(p[0])
#     p = p[1]


# class LinkedList():
#     def __init__(self):
#         self._begin = None

#     def insert(self, x):
#         self._begin = [x, self._begin]

#     def pop(self):
#         assert self._begin is not None, "Empty list"
#         x = self._begin[0]
#         self._begin = self._begin[1]
#         return x

# M = LinkedList()
# M.insert(6)
# M.insert(7)
# M.insert(5)
# print(M.pop())
# print(M.pop())
# print(M.pop())


class Node():
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def append(self, new_data):
        """
        Функция, которая добавляет элемент в конец списка
        """
        new_node = Node(new_data)
        current_node = self.head
        if current_node == None:
            self.head = new_node
            return

        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def insert(self, new_data):
        """
        Функция, которая добавляет элемент в начало списка
        """
        new_node = Node(new_data)
        current_node = self.head

        new_node.next = current_node
        self.head = new_node

    def pop(self):
        """
        Функция, которая удаляет элемент с конца списка
        """
        current_node = self.head

        while current_node.next.next != None:
            current_node = current_node.next
        current_node.next = None

    def show(self):
        """
        Функция, которая выводит весь список
        """
        current_node = self.head
        out = ""
        while current_node != None:
            out += str(current_node.data) + " => "
            current_node = current_node.next
        return out


A = LinkedList()
A.append(5)
A.append(7)
A.append(8)
A.append(9)
A.insert(2)
A.insert(3)
print(A.show())
A.pop()
print(A.show())
A.pop()
print(A.show())
