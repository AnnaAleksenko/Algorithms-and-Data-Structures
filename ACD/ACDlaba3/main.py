def check_brackets(stroka):
    stack = []
    open = ["(", "{", "["]
    close = [")", "}", "]"]

    for i in stroka: # перебираем все символы в заданной строке
        if i in open: # если нашелся элемент соответсвующий из списка open
            stack.append(i) # мы записываем этот элемент в стек
        if i in close: # если нашелся элемент соответсвующий из списка close
            if not stack: # проверяем не пустой ли стек, если он пуст значит открывающеся скобки для нее нет
                return False
            last_opening = stack.pop() #извлекаем последнюю открывающуюся скобку в стеке и присваиваем ее переменной
            if open.index(last_opening) != close.index(i): #проверка индекса открывающейся скобки с индексом закрывающейся
                return False

    return len(stack) == 0 #возвращает `True`, если стек `stack` пустой

stroka = input("Введите строку: ")
if check_brackets(stroka):
    print("Строка существует")
else:
    print("Строка не существует")