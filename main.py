# Стек реализуем на основе списка
class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.isEmpty() is False:
            clear = self.stack.pop()
            return clear

    def peek(self):
        if self.isEmpty() is False:
            last = self.stack[len(self.stack) - 1]
            return last

    def size(self):
        stack_size = len(self.stack)
        return stack_size


# S1 = Stack()
# S1.push(1)
# S1.push(24)
# print(S1.peek())
# print(S1.size())
# print(S1.isEmpty())
# S1.pop()
# print(S1.peek())

# Провекру сбалансированности скобок проще всего произвести добавляя в стек тип скобки при открытии и удаляя при закрытии

def balance_check(text):
    st = Stack()
    opens = "([{〈"
    closes = ")]}〉"

    for bracket in text:
        if bracket in opens:
            st.push(opens.index(bracket))
        elif bracket in closes:
            if st.peek() == closes.index(bracket):
                st.pop()
            else:
                return "Несбалансированно"
    return "Сбалансированно"

# text = '(((([{}]))))'
# text = '[([])((([[[]]])))]{()}'
# text = '{{[()]}}'
text = '}{}'
# text = '{{[(])]}}'
# text = '[[{())}]'

print(balance_check(text))


