def orientation(p, q, r):
    # Функция определения ориентации трех точек
    # Возвращает 0, если точки коллинеарны
    # Возвращает 1, если точки образуют левый поворот
    # Возвращает 2, если точки образуют правый поворот
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def convex_hull(points):
    n = len(points)
    # Если меньше 3 точек, то оболочка уже найдена
    if n < 3:
        return points
    # Находим самую левую и самую правую точки
    leftmost = min(points, key=lambda x: x[0])
    rightmost = max(points, key=lambda x: x[0])
    # Разделяем множество на две части относительно отрезка
    upper = [] # вверх
    lower = [] # низ   # Алгоритма Грэхема
    for p in points:
# если текущая точка является самой левой или самой правой точкой, то она не  в списоке вершин выпуклой оболочки.
        if p == leftmost or p == rightmost:
            continue
# если текущая точка расположена выше отрезка, соединяющего самую левую и самую правую точки, то она будет добавлена в список вершин верхней части выпуклой оболочки
        if orientation(leftmost, p, rightmost) == 1:
            upper.append(p)
        else:
            lower.append(p) #в нижней части
    hull = [leftmost, rightmost]# список вершин выпуклой оболочки начинается с самой левой и самой правой точек.
    # Находим выпуклые оболочки для двух частей
    hull.extend(convex_hull_help(upper, leftmost, rightmost)) # метод .extend() добавляетвсе элементы это списка в конец списка hull
    hull.extend(convex_hull_help(lower, rightmost, leftmost))
    hull = list(set(tuple(i) for i in hull)) # неизменяемый тип данных в Python, который используется для хранения упорядоченной последовательности элементов.
    hull.sort(key=lambda x: (x[0] - leftmost[0]) / (rightmost[0] - leftmost[0]))
    return hull

# список точек, образующих выпуклую оболочку множества points внутри треугольника p1-p2-farthest,  farthest - точка из points, наиболее удаленная от отрезка p1-p2.
def convex_hull_help(points, p1, p2):
    n = len(points)
    if n == 0:
        return []
    if n == 1:
        return [points[0]]
    farthest = max(points, key=lambda x: distance(p1, p2, x))
    left_points = [p for p in points if orientation(p1, farthest, p) == 2]
    right_points = [p for p in points if orientation(farthest, p2, p) == 2]
    hull = []
    hull.extend(convex_hull_help(left_points, p1, farthest))
    hull.extend(convex_hull_help(right_points, farthest, p2))
    hull.append(farthest)
    return hull

def distance(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs((y2-y1)*x3 - (x2-x1)*y3 + x2*y1 - y2*x1) / ((y2-y1)*2 + (x2-x1)*2)**0.5

# Ввод данных
n = int(input("Введите количество точек: "))
points = []
for i in range(n):
    x, y = map(float, input(f"Введите координаты точки {i+1}: ").split())
    points.append([x, y])

# Находим выпуклую оболочку
hull = convex_hull(points)

# Вывод результата

if len(hull) < 3 :
    print("Выпуклая оболочка не существует")
else:
    print("Выпуклая оболочка существует")
    for i in range(len(hull)):
        if i == 0 or i == len(hull)-1 or orientation(hull[i-1], hull[i], hull[i+1]) != 0:
            print(hull[i])






