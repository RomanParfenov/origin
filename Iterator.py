

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None, 4],
    [1, 2, None]

]

estor = [
     ['хурма', 60, 'гр.'],
     ['киви', 60, 'гр.'],
     ['творог', 60, 'гр.'],
     ['сахар', 10, 'гр.'],
     ['мед', 50, 'мл.'],
 ]

class Myrange:

    def __iter__(self):
        return self

    def __init__(self, list):
        self.list = list
        self.counter_one = 0
        self.counter_two = -1

    def __next__(self):
        if (self.counter_one + 1) == len(self.list) and (self.counter_two + 1) == len(self.list[self.counter_one]):
            raise StopIteration

        self.counter_two += 1
        if (self.counter_two) == (len(self.list[self.counter_one])):
            self.counter_one += 1
            self.counter_two = 0
        item = self.list[self.counter_one][self.counter_two]

        return item


s_iter = Myrange(estor)
for i in s_iter:
    print(i)

