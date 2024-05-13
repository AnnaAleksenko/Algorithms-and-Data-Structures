# Импорт модуля deque из библиотеки collections
from collections import deque

# Функция для чтения матрицы смежности из файла
def read_adjacency_matrix(file_path):
    # Открываем файл для чтения
    with open(file_path, 'r') as f:
        # Читаем все строки из файла
        lines = f.readlines()
        matrix = []
        # Обрабатываем каждую строку
        for line in lines:
            # Разбиваем строку на числа, преобразуя их в int, и добавляем в текущую строку матрицы
            row = [int(x) for x in line.split()]
            matrix.append(row)
    return matrix

# Функция для обхода графа в ширину (BFS) с поиском компонент связности
def bfs(graph, start, visited, component):
    # Помечаем стартовую вершину как посещенную
    visited[start] = True
    # Очередь для обхода вершин в BFS
    queue = deque([start])

    # Цикл выполняется, пока очередь не пуста
    while queue:
        # Извлекаем вершину из начала очереди
        vertex = queue.popleft()
        # Добавляем вершину в текущую компоненту связности
        component.append(vertex)
        # Проверяем всех соседей текущей вершины
        for neighbour in range(len(graph)):
            # Если есть ребро между текущей вершиной и соседом и сосед еще не посещен
            if graph[vertex][neighbour] == 1 and not visited[neighbour]:
                # Помечаем соседа как посещенного
                visited[neighbour] = True
                # Добавляем соседа в очередь для дальнейшего обхода
                queue.append(neighbour)

# Функция для поиска компонент связности в графе
def find_connected_components(graph):
    visited = [False] * len(graph)  # Создание списка visited длиной равной количеству вершин в графе, инициализация всех значений как False
    components = []  # Создание пустого списка для хранения компонент связности
    for vertex in range(len(graph)):  # Цикл по всем вершинам графа
        if not visited[vertex]:  # Если текущая вершина еще не была посещена
            component = []  # Создание пустого списка для текущей компоненты связности
            bfs(graph, vertex, visited, component)  # Вызов функции bfs для обхода графа начиная с текущей вершины и поиска компоненты связности
            components.append(component)  # Добавление найденной компоненты связности в список компонент
    return components  # Возвращение списка компонент связности после завершения обхода графа

# Функция для записи компонент связности в файл
def write_components_to_file(file_path, components):
    with open(file_path, 'w') as f:
        f.write('Количество компонент: ' + str(len(components)) + '\n')

        for component in components:
            f.write(' '.join([str(x) for x in component]) + '\n')


if __name__ == '__main__':
    input_file = 'graph.txt'
    output_file = 'output.txt'
    adjacency_matrix = read_adjacency_matrix(input_file)
    components = find_connected_components(adjacency_matrix)
    write_components_to_file(output_file, components)