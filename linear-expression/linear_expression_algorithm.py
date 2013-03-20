import itertools
import operator
import functools
import random

def linear_expression_fun(datas):
    def matrix_multi(vector, data):
        return reduce(operator.__add__, itertools.imap(operator.__mul__, data, vector))

    def distance(data, vector):
        return matrix_multi(vector, data[:-1]) - data[-1]

    # J function is the error function, find the minest value of J, and obtain the vector
    def J(vector):
        return reduce(operator.__add__, map(lambda data: distance(data, vector) ** 2, datas)) / (2 * len(datas))

    def closer(pos, vector, step):
        return vector[pos] - step / len(datas) * reduce(operator.__add__, map(lambda data: distance(data, vector) * data[pos], datas))

    def closers(vector, step):
        return map(lambda pos: closer(pos, vector, step), xrange(len(vector)))

    vector = []
    for i in xrange(len(datas[0])-1):
        vector.append(random.randint(0, 100))
    mins = J(vector)
    while 1:
        vector = closers(vector, 0.0001)
        value = J(vector)
        if mins > value:
            mins = value
        else:
            break

    return functools.partial(matrix_multi, vector)

if __name__ == '__main__':
    datas = [[1,2],[3,6], [7,13],[8,17],[6,11],[9,25],[10,15]]
    fun = linear_expression_fun(datas)
    print fun([50])



