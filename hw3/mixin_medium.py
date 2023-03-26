import numpy as np
import numbers


class WriteToFileMixin:
    def write(self, filename):
        with open(filename, 'w') as f:
            f.write(np.array2string(self._value))


class PrintMixin:
    def __str__(self):
        return np.array2string(self._value)


class GetterSetterMixin:
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if str(type(new_value)) != "<class 'numpy.ndarray'>":
            raise TypeError
        self._value = new_value


class Operators(np.lib.mixins.NDArrayOperatorsMixin,
                WriteToFileMixin, PrintMixin, GetterSetterMixin):
    def __init__(self, value):
        self._value = np.asarray(value)

    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (Operators,)):
                return NotImplemented

        inputs = tuple(x.value if isinstance(x, Operators) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.value if isinstance(x, Operators) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)

    def __repr__(self):
        return '%s(%r)' % (type(self).__name__, self.value)


if __name__ == "__main__":
    np.random.seed(0)

    a_matrix = Operators(np.random.randint(0, 10, (10, 10)))
    b_matrix = Operators(np.random.randint(0, 10, (10, 10)))
    (a_matrix + b_matrix).write("artifacts/medium/matrix+.txt")
    (a_matrix * b_matrix).write("artifacts/medium/matrix_mul.txt")
    (a_matrix @ b_matrix).write("artifacts/medium/matrix@.txt")