"""
Class definition for data structure to be used by the perceptron
"""
class Vector(list):
    """
    Represent a feature vector or a weight vector.
    Inherits from list.

    Feature/weight vectors are lists with operators (*, +, -) defined
    as follows:
    Dot product of two features vectors, f1, f1:  f1 * f2
    Sum of two feature vectors f1:  f1 + f2
    Difference of two feature vectors f1:  f1 - f2
    Note that to be able to use these operators, the two vectors must have
    the same size.
    Argument:
    size (integer): vector size
    """
    def __init__(self, size):
        for i in range(size):
            self.append(0)

    def __mul__(self, other):
        if len(self) != len(other):
            raise TypeError(f'These two vectors have different sizes\n'
                            f'{self}\n{other}')
        else:
            result = sum (self[i] * other[i] for i in range(len(self)))
            return result


    def __add__(self, other):
        size = len(self)
        if size != len(other):
            raise TypeError(f'These two vectors have different sizes\n'
                            f'{self}\n{other}')
        else:
            result = Vector(size)
            for i in range(size):
                result[i] = self[i] + other[i]
            return result

    def __sub__(self, other):
        size = len(self)
        if size != len(other):
            raise TypeError(f'These two vectors have different sizes\n'
                            f'{self}\n{other}')
        else:
            result = Vector(size)
            for i in range(size):
                result[i] = self[i] - other[i]
            return result
