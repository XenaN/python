import numpy as np
import math


class HashMixin:
    def __hash__(self):
        """
        Считает просто норму матрицы, умножая каждый элемент на простое число.
        :return sum: number
        """
        sum = 0
        for i in range(self.m.shape[0]):
            for j in range(self.m.shape[1]):
                sum += self.m[i, j]
        return int(math.sqrt(sum))


class Matrix(HashMixin):
    _cache = {}

    def __init__(self, m):
        self.m = m

    def __str__(self):
        return np.array2string(self.m)

    def __add__(self, other):
        if self.m.shape != other.m.shape:
            raise ValueError

        return self.m + other.m

    def __mul__(self, other):
        if self.m.shape != other.m.shape:
            raise ValueError

        return self.m * other.m

    def __matmul__(self, other):
        if self.m.shape[0] != other.m.shape[1] and \
                self.m.shape[1] != other.m.shape[0]:
            raise ValueError

        if (hash(self), hash(other)) in Matrix._cache:
            return Matrix._cache[(hash(self), hash(other))]

        result = self.m @ other.m
        Matrix._cache[(hash(self), hash(other))] = result
        return result


if __name__ == "__main__":
    np.random.seed(0)

    # EASY
    a_matrix = Matrix(np.random.randint(0, 10, (10, 10)))
    b_matrix = Matrix(np.random.randint(0, 10, (10, 10)))

    with open("artifacts/easy/matrix+.txt", "w") as file:
        file.write(np.array2string(a_matrix + b_matrix))

    # Не дает винда вставлять * в имя
    with open("artifacts/easy/matrix_mul.txt", "w") as file:
        file.write(np.array2string(a_matrix * b_matrix))

    with open("artifacts/easy/matrix@.txt", "w") as file:
        file.write(np.array2string(a_matrix @ b_matrix))

    # HARD
    a = np.random.randint(0, 10, (5, 4))
    b = np.random.randint(0, 10, (4, 5))
    A = Matrix(a)
    B = Matrix(b)
    AB = A@B

    # Хэш на основе нормы будет таким же если в матрице поменять значения местами
    a_0 = a[0, 0]
    a_n = a[4, 3]
    c = np.sort(a.copy(), axis=None).reshape((5, 4))
    d = b.copy()

    C = Matrix(c)
    D = Matrix(b)

    CD = C@D
    Matrix._cache = {}
    CD_real = C@D

    print((hash(A) == hash(C)) and
          (a != c).any() and
          (b == d).all() and
          (a @ b != c @ d).all())

    results = {
        'A': A,
        'B': B,
        'C': C,
        'D': D,
        'AB': AB,
        'CD': CD_real,
        'hash': [hash(Matrix(AB)), hash(Matrix(CD))]
    }
    for name, result in results.items():
        with open(f"artifacts/hard/{name}.txt", "w") as file:
            file.write(str(result))








