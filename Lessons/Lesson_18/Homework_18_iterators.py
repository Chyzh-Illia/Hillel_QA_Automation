class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        result = self.data[self.index]
        self.index -= 1
        return result

reversed_list = ReverseIterator([1, 2, 3, 4])
for item in reversed_list:
    print(item)

class EvenNumbersIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current
        self.current += 2
        return result

even_numbers = EvenNumbersIterator(10)
for number in even_numbers:
    print(number)