# Алгоритм Флойда-Уоршалла
def floyd_warshall(graph, n):
    # Копируем матрицу графа для дальнейших изменений
    dist = [row[:] for row in graph]

    # Основной цикл алгоритма
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Если существует путь через вершину k, проверяем, можно ли улучшить путь
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist