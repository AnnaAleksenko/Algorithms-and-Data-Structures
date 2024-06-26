# Ввод строки поиска с клавиатуры
t = input("Введите строку поиска: ") # образ

# Этап 1: формирование таблицы смещений

S = set()  # уникальные символы в образе
M = len(t)  # число символов в образе
d = {}  # словарь смещений

# Заполняем словарь смещений для каждого символа алфавита
for c in range(256):
    d[chr(c)] = M

# Уточняем смещения для символов образа, кроме последнего
for i in range(M - 1):
    d[t[i]] = M - i - 1

# Этап 2: поиск образа в строке
with open('input.txt', 'r') as f:
    a = f.readline()

N = len(a)

if N >= M:
    i = M - 1  # счетчик проверяемого символа в строке
    matches = []  # список для хранения индексов совпадений

    while (i < N):
        k = 0
        j = M - 1
        while (j >= 0 and a[i - k] == t[j]):  # сравниваем символы с конца образа
            k += 1  # увеличиваем счетчик совпавших символов
            j -= 1  # уменьшаем индекс символа в образе

        if k == M:  # если все символы образа совпали
            matches.append(i - k + 1)  # добавляем индекс начала совпадения в список

        i += d[a[i]]  # сдвигаем образ на значение из таблицы смещений

    if matches:  # если список не пустой
        print(f"образ найден по индексам {matches}")
    else:
        print("образ не найден")
else:
    print("образ не найден")
