from collections import deque 
search_queue = deque()

graph = {}
graph["cab"] = ["cat", "car"]
graph["car"] = ["bar", "cat"]
graph["bar"] = ["bat"]
graph["cat"] = ["bat","mat"]
graph["mat"] = ["bat"]
graph["bat"] = []




""" 
Поиск в ширину. Функция перебирает все узлы графа, пока не выполнится условие, 
либо пока есть, что перебирать. В данном случае используется "очередь" deque(). В качестве
опорной точки выступает нулевой элемент списка deque(), и он сравнивается с заданным условием.
Функция не проверяет дважды один и тот же элемент списка.

"""

def search_queue(start, end):
    search_queue = deque()
    search_queue += graph[start]
    searched = []

    while search_queue:
        object_name = search_queue.popleft()
        if not object_name in searched:
            if end == object_name:
                return "Это то, что нам нужно!"
            else:
                search_queue += graph[object_name]
                search_queue.append(object_name)
    return False
                

print(search_queue("cab", "bat"))









