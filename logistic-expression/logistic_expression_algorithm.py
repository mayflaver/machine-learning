import functools
import random
import itertools
import operator
import math

def logistic_expression_fun(datas):
    def matrix_multi(vector, data):
        return reduce(operator.__add__, itertools.imap(operator.__mul__, data, vector))

    def p_help(vector, data):
            return 1.0 / (1.0 + math.e ** (-matrix_multi(vector, data[:-1])))

    def probility(vector, data):
        if data[-1] == 1:
            return p_help(vector, data)
        else:
            return 1 - p_help(vector, data)

    def J(vector):
        return math.log(reduce(operator.__mul__, map(lambda data: probility(vector, data), datas)))

    def closer(pos, vector, step):
        return vector[pos] - step * reduce(operator.__mul__, map(lambda data: (data[-1] - p_help(vector, data)) * data[pos]))

    def closers(vector, step):
        return map(lambda pos: closer(pos,vector, step), xrange(len(vector)))

    vector = []
    for i in xrange(len(datas[0]) - 1):
        vector.append(random.randint(0, 100))

    maxs = J(vector)
    while 1:
        vector = closer(vector, 0.00001)
        value = J(vector)
        if maxs < value:
            maxs = value
        else:
            break

    return functools.partial(probility, vector)


if __name__ == '__main__':
    datas = [[1,1],[2,1],[3,1],[4,1],[6,1], [5,0],[7,0],[8,0],[9,0]]
    fun = logistic_expression_fun(datas)
    print fun([10])
            
                    
            
            
