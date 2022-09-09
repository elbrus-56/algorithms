""" 
Поиск в ширину. 
Поиск в ширину вычисляет кратчайший путь в невзвешенном графе.

Применяется для:
- определения кратчайших путей и минимальных остовных деревьев;
- индексации веб-страниц поисковыми ботами;
- поиска в соцсетях;
- нахождения доступных соседних узлов в одноуровневых сетях, таких как BitTorrent.

Функция перебирает все узлы графа, пока не дойдет до конца, либо пока не выполнится 
условие.
Функция не проверяет дважды один и тот же элемент списка.

"""


from collections import deque 
search_queue = deque()

graph = {}
graph["cab"] = ["cat", "car"]
graph["car"] = ["bar", "cat"]
graph["bar"] = ["bat"]
graph["cat"] = ["bat","mat"]
graph["mat"] = ["bat"]
graph["bat"] = []




def search_queue(start):
    search_queue = deque()
    search_queue += graph[start]
    visited = [start]

    while search_queue:
        object_name = search_queue.popleft()
        if not object_name in visited:
                search_queue += graph[object_name]
                visited.append(object_name)
    return visited
                

print(search_queue("cab"))


def bfs(graph, node):
    visited = [node]
    queue = [node]
    while queue:
        s = queue.pop(0)
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited

print(bfs(graph, 'cab'))





