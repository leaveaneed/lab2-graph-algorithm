# Функция для чтения графа из файла
def read_graph(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())  # количество вершин
        # Инициализация матрицы смежности
        graph = [[float('inf')] * n for _ in range(n)]
        
        # Расстояние до самой себя для каждой вершины = 0
        for i in range(n):
            graph[i][i] = 0
        
        # Чтение рёбер
        for line in file:
            u, v, w = map(int, line.split())
            graph[u][v] = w  # Устанавливаем вес ребра между вершинами u и v
    
    return graph, n

# Функция для записи результата в файл
def write_result(filename, dist, n):
    with open(filename, 'w') as file:
        for i in range(n):
            for j in range(n):
                if dist[i][j] == float('inf'):
                    file.write("INF ")  # Если нет пути, записываем "INF"
                else:
                    file.write(f"{dist[i][j]} ")  # Записываем расстояние
            file.write("\n")  # Переход на следующую строку после каждой строки матрицы
