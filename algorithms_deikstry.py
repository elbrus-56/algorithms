"""
Алгоритм Дейкстры работает только с направленными ациклическими графами.
Использование алгоритма Дейкстры с графом, содержащим ребра с 
отрицательным весом, невозможно.

"""

node = find_lowest_cost_node(costs) 
while node is not None:

    cost = costs[node] 
    neighbors = graph[node] 
    for n in neighbors.keys():
        new_cost = cost + neighbors[n] 
        if costs[ n] > new_cost:
            costs[n] = new_cost 
            parents[n] = node 
            processed.append(node) 
            node = find_lowest_cost_node(costs) 