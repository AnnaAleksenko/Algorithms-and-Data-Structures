class Stack():
    def __init__(self):
        self.elements = []
    def push(self, element):
        self.elements += [element]
    def pop(self):
        return self.elements.pop()
    def get_element(self):
        return self.elements[-1]



def check_line(stack, line):
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    for element in line:
        if element in opening:
            stack.push(element)
        elif element in closing:
            if len(stack.elements) == 0:
                return "Некорректная строка"
            if element == closing[opening.index(stack.get_element())]:
                #print(f"element - {element} | closing {closing[closing.index(element)]}")
                stack.pop()
            else:
                return "Некорректная строка"
        else:
            return "Строка содержит не только скобки"
    if len(stack.elements) > 0:
        return "Некорректная строка"
    return "Строка корректная"
def main():
    stack = Stack()
    print("Введите строку: ")
    line = input()
    if line != '':
        print(check_line(stack, line))
    else:
        print("Строка пустая")

if __name__ == "__main__":
    main()