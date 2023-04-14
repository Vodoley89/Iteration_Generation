# list_of_lists = [[1, 2, 3],['a', 'b', 'c'],[{1: 'qwerty'}]
#                  ]
from cloudpickle import instance

list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]


class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists_1
        self.start = -1
        self.end = len(self.list_of_lists[self.start])




    def __iter__(self):
        self.start += 1
        self.cursor = 0
        return self



    def __next__(self):
        if self.cursor == len(self.list_of_lists[self.start]):
            iter(self)
        if self.start == self.end:
            raise StopIteration
        self.cursor += 1
        return self.list_of_lists[self.start][self.cursor - 1]


if __name__ == '__main__':
    new_lst = [elem for elem in FlatIterator(list_of_lists_1)]
    print(new_lst)


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    return FlatIterator(list_of_lists_1)

if __name__ == '__main__':
    test_1()
