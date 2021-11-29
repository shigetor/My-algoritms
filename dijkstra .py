import math

"""алгоритм дейкстры"""


def funcMin(X, Y):
    value = -1
    m = math.inf
    for i, t in enumerate(X):
        if t < m and i not in Y:
            m = t
            value = i

    return value


graph = ((0, 3, 1, 3, math.inf, math.inf),
         (3, 0, 4, math.inf, math.inf, math.inf),
         (1, 4, 0, math.inf, 7, 5),
         (3, math.inf, math.inf, 0, math.inf, 2),
         (math.inf, math.inf, 7, math.inf, 0, 4),
         (math.inf, math.inf, 5, 2, 4, 0))

num_top = len(graph)  # количество вершин
last = [math.inf] * num_top  # последняя строка таблицы

start_top = 0  # начальная вершина
top = {start_top}  # просмотренные вершины
last[start_top] = 0  # вес начальной вершины
conn = [0] * num_top  # связь между вершинами

while start_top != -1:
    for val1, val2 in enumerate(graph[start_top]):  # перебираем все связанные вершины с вершиной v
        if val1 not in top:
            top1 = last[start_top] + val2
            if top1 < last[val1]:
                last[val1] = top1
                conn[val1] = start_top  # связываем вершину j с вершиной v

    start_top = funcMin(last, top)  # находим узел с меньшим весом
    if start_top >= 0:
        top.add(start_top)  # рассматриваем следующую вершину

# нахождение пути
start = 0
end = 4
result = [end]
while end != start:
    end = conn[result[-1]]
    result.append(end)

print(result)

