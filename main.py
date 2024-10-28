from graph_io import read_graph, write_result
from floyd_warshall import floyd_warshall
from utils import print_matrix

# Основная функция программы
def main(input_file, output_file):
    try:
        # Чтение графа из файла
        graph, n = read_graph(input_file)
        print("Граф успешно загружен. Матрица смежности:")
        print_matrix(graph, n)
        
        # Применение алгоритма Флойда-Уоршалла
        dist = floyd_warshall(graph, n)
        print("\nМатрица кратчайших расстояний после применения алгоритма Флойда-Уоршалла:")
        print_matrix(dist, n)
        
        # Запись результатов в файл
        write_result(output_file, dist, n)
        print(f"\nРезультаты записаны в файл: {output_file}")

    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример запуска программы
if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    main(input_file, output_file)
