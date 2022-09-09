# Оригинал статьи: https://www.python.org/doc/essays/graphs/

"""
Граф - это структура данных, состоящая из узлов, соединенных ребрами или дугами.
В ориентированных графах связи между узлами имеют направление, в неориентированных не имеют. 
Графы бывают двунаправленные и однонаправленные. 
"""


graph = {}
graph["cab"] = ["cat", "car"]
graph["car"] = ["bar", "cat"]
graph["bar"] = ["bat"]
graph["cat"] = ["bat","mat"]
graph["mat"] = ["bat"]
graph["bat"] = []


# Функция, которая ищет путь из начала в конец в однонаправленном графе
# с помощью рекурсии. Один узел встречается только один раз.

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    elif not graph[start]:
        return None
    else:
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath:
                    return newpath
    return None

# print(find_path(graph, 'cab', 'bat'))


# Функция, которая ищет все пути с помощью рекурсии

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    elif not graph[start]:
        return []
    else:
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
    return paths

for i in enumerate(find_all_paths(graph, 'cab', 'bat'), start=1):
    print(i)
