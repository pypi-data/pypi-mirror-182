import math

LAST = -1
FIRST = 0

def cos(a):
    return math.cos(math.radians(a))

def sin(a):
    return math.sin(math.radians(a))

def sgn(a):
    return a/abs(a) if a != 0 else 0

class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def check_instance(fun):
        def wrap(self, other):
            if not isinstance(other, Vector):
                raise TypeError("types don't match")
            return fun(self, other)
        return wrap

    @check_instance
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    @check_instance
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Vector(self.x / other, self.y / other)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __str__(self):
        return "Vector object with coords ({}, {})".format(self.x, self.y)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __iter__(self):
        return iter((self.x, self.y))

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    @property
    def unit(self):
        return self / abs(self) if abs(self) != 0 else Vector.ZERO()

    @classmethod
    def ZERO(cls):
        return cls(0, 0)

class DataSet: 
    def __init__(self, data: list[list] = list()):
        if isinstance(data, list):
            self.data_ = data.copy()
        else:
            raise ValueError("can not get data")
    
    def __iter__(self):
        return iter(self.data_)

    def append(self, value1, value2):
        self.data_.append((value1, value2))
        return self

    def differentiate(self, index = LAST):
        if len(self.data_) < 2:
            return 0
        if index == LAST:
            return (self.data_[index][1] - self.data_[index - 1][1]) / (self.data_[index][0] - self.data_[index - 1][0])
        elif index == FIRST:
            return (self.data_[index + 1][1] - self.data_[index][1]) / (self.data_[index + 1][0] - self.data_[index][0])
        else:
            return (self.data_[index + 1][1] - self.data_[index - 1][1]) / (self.data_[index + 1][0] - self.data_[index - 1][0])

    def regression(self):
        x_mean = sum(dot[0] for dot in self.data_) / len(self.data_)
        y_mean = sum(dot[1] for dot in self.data_) / len(self.data_)
        a = sum((x - x_mean) * (y - y_mean) for (x, y) in self.data_) / sum((x - x_mean) ** 2 for (x, y) in self.data_)
        b = y_mean - a * x_mean
        return (a, b)

    def math_function(self):
        n = len(self.data_) - 1
        rows = list()
        for i in range(n + 1):
            row = list()
            for j in range(n):
                val = self.data_[i][0] ** (n - j)
                row.append(val)
            row.extend((1, self.data_[i][1]))
            rows.append(row.copy())
        matrix = Matrix(*rows)
        for i in range(n):
            for j in range(i, n):
                matrix.multiple_row(j + 2, -matrix[i + 1, i + 1]/matrix[i + 1, j + 2])
                matrix.add_rows(j + 2, i + 1)
        for i in range(n + 1, 0, -1):
            matrix[n + 2, i] = round((matrix[n + 2, i] - sum(matrix[0, i][i:n + 1]))/matrix[i, i], 3)
            for j in range(i - 1, 0, -1):
                matrix[i, j] = matrix[i, j] * matrix[n + 2, i]
        parts = list()
        for i in range(1, n + 2):
            if (i == n + 1) and abs(matrix[n + 2, i]) >= 0.001:
                parts.append(str(matrix[n + 2, i]))
            elif (i == n) and abs(matrix[n + 2, i]) >= 0.001:
                parts.append("{}x".format(matrix[n + 2, i])) 
            elif abs(matrix[n + 2, i] - 0) <= 0.001:
                continue
            elif abs(matrix[n + 2, i] - 1) <= 0.001:
                parts.append("x^{}".format(n + 1 - i)) 
            else:
                parts.append("{}x^{}".format(matrix[n + 2, i], n + 1 - i)) 
        equation = ' + '.join(parts)
        print("Your equation is {}".format(equation))
        return equation     

class Matrix:
    def __init__(self, *args):
        self.data = list(args)

    def __getitem__(self, key):
        if isinstance(key, tuple):
            x, y = key
            if x == 0:
                return self.data[y - 1]
            if y == 0:
                column = list(self.data[i][x - 1] for i in range(len(self.data)))
                return column
            return self.data[y - 1][x - 1]
        else:
            raise ValueError("index must be a tuple")

    def __setitem__(self, key, arg):
        if isinstance(key, tuple):
            x, y = key
            if x == 0:
                self.data[y - 1] = arg
            elif y == 0:
                for i in range(len(arg)):
                    self.data[i][x - 1] = arg[i]
            else:
                self.data[y - 1][x - 1] = arg
        else:
            raise ValueError("index must be a tuple")
        return self

    def reverse(self):
        columns = list(self[i + 1, 0] for i in range(len(self[0, 1])))
        return Matrix(*columns)

    def __str__(self):
        str_rows = list(map(lambda row: " ".join(map(str, row)), self.data))
        return "\n".join(str_rows)

    def add_rows(self, main: int, other: int):
        self[0, main] = list(self[0, main][i] + self[0, other][i] for i in range(len(self[0, main])))
        return self

    def substract_rows(self, main: int, other: int):
        self[0, main] = list(self[0, main][i] - self[0, other][i] for i in range(len(self[0, main])))
        return self

    def multiple_row(self, main: int, n: float):
        self[0, main] = list(map(lambda k: k * n, self[0, main]))
        return self

    def negate_row(self, main: int):
        self[0, main] = list(map(lambda k: -k, self[0, main]))
        return self

    def __iter__(self):
        return iter(sum(self.data))

    @classmethod
    def ZERO(cls, x: int, y: int):
        row: list = [0] * x
        rows = [row.copy() for i in range(y)]
        return cls(*rows)