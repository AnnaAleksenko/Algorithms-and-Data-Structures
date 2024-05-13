""""
# Пункт 1:

#def check_brackets(expression):
stack = []

print(stack)
#for char in expression:

if char == "(":
stack.append(char)
elif char == ")":
if len(stack) == 0 or stack.pop() != "(":
return False

return len(stack) == 0

# Пример использования
user_input = input("Введите строку: ")
if check_brackets(user_input):
print("Строка существует")
else:
print("Строка не существует")
```

#Пункт 2:

#def check_brackets(expression):
stack = []

#for char in expression:
if char in "([{":
stack.append(char)
elif char in ")]}":
if len(stack) == 0 or not is_matching(stack.pop(), char):
return False

return len(stack) == 0

def is_matching(open_bracket, close_bracket):
return (open_bracket == "(" and close_bracket == ")") or \ (open_bracket == "[" and close_bracket == "]") or \ (open_bracket == "{" and close_bracket == "}")

# Пример использования
user_input = input("Введите строку: ")
if check_brackets(user_input):
print("Строка существует")
else:
print("Строка не существует")

"""
from math import log

# Лабораторная работа № 3 (Задача о простых множителях)
print("Введите число:")
x = int(input())
a3 = int(log(x, 3))  # логарифм x по основанию 3
a5 = int(log(x, 5))
a7 = int(log(x, 7))
for k in range(a3 + 1):
    for l in range(a5 + 1):
        for m in range(a7 + 1):
            a = 3 ** k * 5 ** l * 7 ** m
            if a <= x:
                print(a)
