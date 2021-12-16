
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not compare(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        print(f'Сбалансированно')
    else:
        print(f'Несбалансированно')

# Фу-ция сравнения идентичности противоположных символов
def compare(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

if __name__ == '__main__':
    parChecker('{{([][])}()}')
    parChecker('{{}')