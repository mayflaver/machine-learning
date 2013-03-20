import itertools
import operator
import functools
import random

def matrix_multi(vector, data):
    return reduce(operator.__add__, itertools.imap(operator.__mul__, data, vector))

def linear_expression_fun(datas):
    def matrix_multi(data, vector):
        return reduce(operator.__add__, itertools.imap(operator.__mul__, data, vector))

    def help_fun(pos, datas, vector, step):
        return vector[pos]- step*reduce(operator.__add__, map(lambda data: (matrix_multi(data[:-1], vector)-data[-1])*data[pos]))/len(datas)

    def iterator(pos, vector):
        return map(lambda pos, vector: help_fun(pos, datas, vector, step), vector)

    def vector_again(vector):
        return map(lambda pos: iterator(pos, vector), xrange(len(vector)))

    def J(vector, datas):
        reduce(operator.__add__, map(lambda data: matrix_multi(init, data[:-1])-data[-1], datas))
    init = []
    for i, _ in enumerate(datas[0][:-1]):
        init.append(random.randint(0, 100))
        
        
    J_value = J(init)
    while True:
        init = vector_again(init)
        if J_value - J(init) > 0.001:
            J_value = J(init)
            
        else:
            break
    return functools.partial(matrix_multi, init)
    

    
