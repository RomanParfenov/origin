

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


def my_generator(list):
    for item in list:
        for goods in item:
            yield goods



s_iter = my_generator(estor)

for i in s_iter:
    print(i)