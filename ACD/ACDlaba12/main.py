import heapq
import os

# В первой фазе алгоритма происходит чтение входного файла построчно.
# Каждая строка интерпретируется как последовательность чисел,
# которые разделяются и сохраняются в блоки размером block_size.
# Затем каждый блок сортируется по возрастанию и записывается во временные файлы с именами block_{block_num}.txt,
# где block_num - номер блока.
def external_sort(input_file, output_file, block_size):
    # Phase 1: Разделение на блоки и их сортировка
    with open(input_file, 'r') as file:
        block_num = 0
        while True:
            block = []
            line = file.readline()
            if not line:
                break
            numbers = list(map(int, line.strip().split()))
            for i in range(0, len(numbers), block_size):
                number = numbers[i:i+block_size]
                block.append(number)
            if not block:
                break
            for i in range(len(block)):
                block[i].sort()
                mini_block = block[i]
                with open(f'block_{block_num}.txt', 'w') as block_file:
                    numbers_str = ' '.join(map(str, mini_block))
                    block_file.write(numbers_str)
                block_num += 1


# Во второй фазе алгоритма блоки сливаются в итоговый отсортированный файл.
# Создается пустая куча (heap), и для каждого блока открывается соответствующий временный файл.
# Из каждого файла считывается первое число, добавляется в кучу с указанием индекса блока.
# Затем из кучи извлекается наименьшее число, записывается в выходной файл (output_file),
# и из того же блока считывается следующее число, которое затем добавляется в кучу.
# Процесс продолжается до тех пор, пока куча не опустеет.

    # Phase 2: Слияние блоков
    heap = []
    with open(output_file, 'w') as output:
        block_files = [open(f'block_{i}.txt', 'r') for i in range(block_num)]
        for i, block_file in enumerate(block_files):
            line = block_file.readline().strip()
            num = list(map(int, line.strip().split()))
            print(num)
            if num:
                for j in range(len(num)):
                    heapq.heappush(heap, (int(num[j]), i))

        while heap:
            smallest, block_index = heapq.heappop(heap)
            output.write(str(smallest) + '\n')
            if not block_files[block_index].closed:
                next_num = block_files[block_index].readline().strip()
            if next_num:
                heapq.heappush(heap, (int(next_num), block_index))
            else:
                block_files[block_index].close()

    # Удаление временных файлов блоков
    for i in range(block_num):
        file_name = f'block_{i}.txt'
        os.remove(file_name)

external_sort('input.txt', 'output.txt', block_size=20)