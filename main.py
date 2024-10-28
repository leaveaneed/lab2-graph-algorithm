from graph_io import read_graph, write_result
from floyd_warshall import floyd_warshall
from utils import print_matrix

# Основная функция программы
def main(input_file, output_file):
    graph, n = read_graph(input_file)  # Чтение графа из файла
    dist = floyd_warshall(graph, n)    # Применение алгоритма Флойда-Уоршалла
    write_result(output_file, dist, n)  # Запись результатов в файл

# Пример запуска программы
if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    main(input_file, output_file)
