from FIRST import check_line, Stack

class calculator():
    def calculte(self, expression):
        s = Stack()
        print(expression)
        expression = expression.replace('(-', '(0-')
        if check_line(s, ''.join([i for i in expression if i in ['(', ')']])) in ["Некорректная строка", "Строка пустая"]\
                or any(map(lambda k: expression.find(k) != -1, [i+j for j in ["-", "+", "*", "/", "="] for i in ["-", "+", "*", "/", "="]])):
            return "Ошибочно составлена строка или строка пустая"
        operators = ['*', '/', '+', '-', '(', ')']
        stack = []
        result = []
        last_s = ''
        for s in expression:
            if s not in operators and s != '=' and last_s not in operators and last_s != '':
                result[-1] = result[-1] + s
                last_s = s
                continue
            last_s = s
            if s in operators:
                self.ensure(s, stack, result)
            elif s == '=':
                if len(stack) != 0:
                    while len(stack) != 0:
                        result += [stack.pop()]
                return self.read_postfix(result)
            else:
                result.append(s)
        if len(stack) != 0:
            while len(stack) != 0:
                result += [stack.pop()]
        return self.read_postfix(result)

    def ensure(self, s, stack, result):
        s_priority = self.get_priority(s)
        if s == '(':
            stack += [s]
            return
        elif s == ')':
            while len(stack) != 0:
                last = stack.pop()
                if last == '(':
                    break
                result += [last]
            return
        if len(stack) != 0:
            last = stack[-1]
            last_priority = self.get_priority(last)
            if last_priority >= s_priority:
                while(len(stack) != 0):
                    if self.check_priority(stack[-1], s):
                        result.append(stack.pop())
                    else:
                        break
                stack += [s]
            else:
                stack += [s]
                return True
        else:
            stack += [s]
            return True

    def get_priority(self, s):
        priority = None
        if s == '/' or s == '*':
            priority = 3
        elif s == "+" or s == '-':
            priority = 2
        else:
            priority = 1
        return priority

    def check_priority(self, f, s):
        if self.get_priority(f) >= self.get_priority(s):
            return True
        return False

    def read_postfix(self, postfix):
        operators = ['*', '/', '+', '-', '(', ')']
        stack = []
        for s in postfix:
            if s not in operators:
                stack += [s]
            else:
                stack[-2] = self.do_operation(stack, s)
                stack.pop()
        return stack[0]

    def do_operation(self, stack, operation):
        try:
            if operation == '+':
                return float(stack[-2]) + float(stack[-1])
            elif operation == '-':
                return float(stack[-2]) - float(stack[-1])
            elif operation == '*':
                return float(stack[-2]) * float(stack[-1])
            elif operation == '/':
                return float(stack[-2]) / float(stack[-1])
        except ZeroDivisionError:
            print("Делить на ноль нельзя. Неправильно составлено выражение")
            exit(1)





def main():
    calc = calculator()
    print(calc.calculte("(-170+2*5)/(5)-5-2*(-31)="))


if __name__ == "__main__":
    main()
