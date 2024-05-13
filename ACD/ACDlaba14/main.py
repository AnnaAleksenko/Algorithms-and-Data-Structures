import csv

# Определяем хеш-функцию
def hash_function(key):
    # Например, простейшая функция - длина ключа
    return len(key)

# Читаем текстовый файл и создаем хеш-таблицу
hash_table = {}
with open('text.txt', 'r') as file:
    for line in file:
        # Разбиваем строку на слова
        words = line.strip().split()
        for word in words:
            # Вычисляем ключ для слова
            key = hash_function(word)
            # Добавляем слово в соответствующий список в хеш-таблице
            if key in hash_table:
                hash_table[key].append(word)
            else:
                hash_table[key] = [word]

# Записываем хеш-таблицу в CSV файл
with open('hash_table.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for key in hash_table:
        writer.writerow([key] + hash_table[key])
