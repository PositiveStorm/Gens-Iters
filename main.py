# Задача №1. Итератор

nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
]

class FlatIterator:
    def __init__(self, mylist):
        self.list = mylist
        self.cursor = -1
        self.list_cursor = 0

    def __iter__(self):
        self.cursor += 1
        self.list_cursor = 0
        return self

    def __next__(self):
        while self.cursor - len(self.list) and self.list_cursor == len(self.list[self.cursor]):
          iter(self)

        if self.cursor == len(self.list):
          raise StopIteration

        self.list_cursor += 1
        return self.list[self.cursor][self.list_cursor - 1]

if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)


# Задача №2. Генератор

def flat_generator(mylist):
    for item in mylist:
        for el in item:
            yield el




for item in flat_generator(nested_list):
    print(item)

