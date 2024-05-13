import hashlib
import csv

# Открываем файл с текстом
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Создаем хеш-функцию
def hash_func(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Создаем пустую хеш-таблицу с наложением
table = {}

# Заполняем хеш-таблицу
for word in text.split():
    key = hash_func(word)
    if key not in table:
        table[key] = set()
    table[key].add(word)

# Записываем хеш-таблицу в файл
with open('table.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Хеш', 'Слова'])
    for key, words in table.items():
        writer.writerow([key, ', '.join(words)])
